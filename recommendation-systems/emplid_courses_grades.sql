select fscc.Emplid , scc.Courses , fscc.Course_Grade_Official as Grades 
from USR_mehdi_karamollahi.dbo.F_Student_Courses_And_Credits as fscc
join USR_mehdi_karamollahi.dbo.f_Course as Course
on fscc.Crse_Strm_Dkey = Course.Crse_Strm_Dkey 
join USR_mehdi_karamollahi.dbo.t_science_courses scc 
on Course.Subject = left(scc.Courses, 4)
and Course.Catalog_Nbr = stuff(scc.Courses, 1, 4, '')
where left(fscc.Strm_Class_Dkey, 4) >= '2137'
and fscc.Repeat_Code != 'LOW' 
and fscc.Course_Status in ('Completed', 'Transfer Credit', 'Other')
order by fscc.Emplid , Courses;