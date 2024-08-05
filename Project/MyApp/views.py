from django.shortcuts import render
from .models import EmpD
from .resources import EmpDResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
import csv, io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def upload(request):
    if request.method == 'POST':
        EmpD_resource = EmpDResource()
        dataset = Dataset()
        new_EmpD = request.FILES['myfile']
        
        if not new_EmpD.name.endswith('csv'):
            messages.info(request, 'Please Upload a CSV File')
            return render(request, 'home.html')
        else:
            messages.info(request, 'File Successfully Uploaded')
        
        data_set = new_EmpD.read().decode('UTF-8')
        io_string = io.StringIO(data_set)

        df = pd.read_csv(io_string, delimiter=',', quotechar='|')
        df_html = df.head().to_html(classes='table table-striped')

        io_string.seek(0)
        next(io_string)  
        
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = EmpD.objects.update_or_create(
                EId=column[0],
                Gender=column[1],
                Experience=column[2],
                Position=column[3],
                Salary=column[4]
            )
        # ------------------------------------------------------------
        web_developers = df[df['Position'] == 'Web Developer']     
        avg_web_dev = round(web_developers['Salary'].mean(),2)
        
        DevOps_Eng = df[df['Position'] == 'DevOps Engineer']     
        Avg_DevOps_Eng = round(DevOps_Eng['Salary'].mean(),2)
        
        Sys_Admin = df[df['Position'] == 'Systems Administrator']     
        avg_sys_adm = round(Sys_Admin['Salary'].mean(),2)
        
        web_developers = df[df['Position'] == 'Web Developer']     
        avg_web_dev = round(web_developers['Salary'].mean(),2)
        
        it_security_analysts = df[df['Position'] == 'IT Security Analyst']
        avg_it_security_analyst = round(it_security_analysts['Salary'].mean(), 2)
        
        managers = df[df['Position'] == 'IT Manager']
        avg_manager = round(managers['Salary'].mean(), 2)

        
        web_developers = df[df['Position'] == 'Web Developer']     
        avg_web_dev = round(web_developers['Salary'].mean(),2)
        min_sal_WebD = web_developers['Salary'].min()
        
        std_experience = df['Experience'].std()
        avg_experience = round(df['Experience'].mean())
        
        max_salary = df['Salary'].max()
        positions_with_max_salary = df[df['Salary'] == max_salary]['Position'].unique()
        
        filtered_df = df[df['Experience'] > 15]
        avg_salary = round(filtered_df['Salary'].mean(),2)
        
        filtered_df2 = df[df['Experience'] < 5]
        avg_salary2 =round(filtered_df2['Salary'].mean(),2)
# "-------------------------------------------------------------------------------------------------------------"
        #Count Plot
         
        gender_counts = df.groupby(['Position', 'Gender']).size().unstack()
        fig, ax = plt.subplots(figsize=(5, 3))
        gender_counts.plot(kind='bar', stacked=True, ax=ax)
        ax.set_xlabel('Position')
        ax.set_ylabel('Count')
        ax.set_title('Gender Distribution by Position')
            
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
            
        graphicd = base64.b64encode(image_png)
        graphic = graphicd.decode('utf-8')
        
# ------------------------------------------------------------------------------------------------------------------  
        # Bar Plot
        
        software_engineers = df[df['Position'] == 'Software Engineer']
        experience_salary = software_engineers.groupby('Experience')['Salary'].mean().reset_index()
        plt.figure(figsize=(5, 3))
        plt.bar(experience_salary['Experience'], experience_salary['Salary'], color='blue')
        plt.xlabel('Experience')
        plt.ylabel('Average Salary')
        plt.title('Average Salary by Experience for Software Engineers')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphics = base64.b64encode(image_png)
        graphic1 = graphics.decode('utf-8')

# ---------------------------------------------------------------------------------------------------------------------        
        # Pie Chart
        
        dba_data = df[df['Position'] == 'Database Administrator (DBA)']
        gender_distribution = dba_data['Gender'].value_counts()
        plt.figure(figsize=(5, 5))
        plt.pie(gender_distribution, labels=gender_distribution.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=140)
        plt.title('Gender Distribution for Database Administrators')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic2 = base64.b64encode(image_png).decode('utf-8')
        
# -----------------------------------------------------------------------------------------------------------------------        
        # Boxplot
        
        plt.figure(figsize=(5, 5))
        sns.boxplot(x='Gender', y='Salary', data=df)
        plt.title('Salary Distribution by Gender')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        box_plot_graphic = base64.b64encode(image_png).decode('utf-8')

# ------------------------------------------------------------------------------------------------------------------------
        # Pie Plot
        
        filtered_df = df[df['Salary'] < 100000]
        gender_counts = filtered_df['Gender'].value_counts()

        plt.figure(figsize=(7, 5))
        plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
        plt.title('Gender Distribution for Salaries Less Than 100,000')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        pie_chart_graphic = base64.b64encode(image_png).decode('utf-8')
 
# ---------------------------------------------------------------------------------------------------------------------------        
        # CountPlot
        
        plt.figure(figsize=(10, 8))
        sns.countplot(y='Position', data=df, palette='viridis')

        plt.title('Count of Employees by Position')
        plt.xlabel('Number of Employees')
        plt.ylabel('Position')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        countplot_position_graphic = base64.b64encode(image_png).decode('utf-8')
        
# -------------------------------------------------------------------------------------------------------------------------------        
        
        context = {
            'df_html': df_html,
            'Total_R': len(df),
            'avg_web_dev': avg_web_dev,
            'DevOps_Eng' : Avg_DevOps_Eng,
            'sys_admin' : avg_sys_adm,
            'std_exp' :std_experience,
            'avg_exp' :avg_experience,
            'min_sal_WebD' : min_sal_WebD,
            'avg_salary' : avg_salary,
            'max_salary': max_salary,
            'positions_with_max_salary': positions_with_max_salary,
            'avg_it_security_analyst' : avg_it_security_analyst,
            'avg_manager': avg_manager,
            'graphic' : graphic,
            'graphic1': graphic1,
            'graphic2': graphic2,
            'box_plot_graphic' :box_plot_graphic,
            'pie_chart_graphic': pie_chart_graphic,
            'countplot_position_graphic': countplot_position_graphic,
            'avg_salary2' : avg_salary2,
        }
        
        
        return render(request, 'home.html', context)
    
    return render(request, 'home.html')
