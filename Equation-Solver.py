import streamlit as st
import numpy as np
from scipy.optimize import fsolve
from scipy.linalg import solve
st.title("Algebraic equation solver")

opt=st.selectbox("Choose what equation you want to solve:",["Linear","Quadratic","Cubic","System of linear equations"])
if opt=="Linear":
    st.header("Solve a linear equation:")
    st.write("Equation format: ax+b=0")
    a=st.number_input("Enter coefficient a here:",value=1)
    b=st.number_input("Enter coefficient b here:",value=1)

    def linear(x):
        eqn=a*x+b
        return eqn
    soln=fsolve(linear,0)
    if st.button("Answer"):
        st.write(f"The root of the equation is {soln}")

elif opt=="Quadratic":
    st.header("Solve a quadratic equation")
    st.write("Equation format: ax^2+bx+c")
    a=st.number_input("Enter coefficient a here:",value=1)
    b=st.number_input("Enter coefficient b here:",value=1)
    c=st.number_input("Enter coefficient c here:",value=1)

    def quadratic(x):
        eqn=a*x**2+b*x+c
        return eqn
    soln=fsolve(quadratic,[0,0])
    if st.button("Answer"):
        st.write(f"The roots of the equation are {soln[0]} and {soln[1]}")

elif opt=="Cubic":
    st.header("Solve a cubic equation")
    st.write("Equation format: ax^3+bx^2+cx+d")
    a=st.number_input("Enter coefficient a here:", value=1)
    b=st.number_input("Enter coefficient b here:", value=1)
    c=st.number_input("Enter coefficient c here:", value=1)
    d=st.number_input("Enter coefficient d here:", value=1)

    def cubic(x):
        eqn=a*x**3+b*x**2+c*x+d
        return eqn
    soln=fsolve(cubic,[0,0,0])
    if st.button("Answer"):
        st.write(f"The roots of the equation are {soln[0]},{soln[1]} and {soln[2]}")


elif opt=="System of linear equations":
    st.header("Solve a system of linear equations")
    st.write("Equation format: Equation 1: ax+by=c, Equation 2:dx+ey=f")
    a=st.number_input("Enter coefficient a here:", value=1)
    b=st.number_input("Enter coefficient b here:", value=1)
    c=st.number_input("Enter coefficient c here:", value=1)
    d=st.number_input("Enter coefficient d here:", value=1)
    e=st.number_input("Enter coefficient e here:",value=1)
    f=st.number_input("Enter coefficient f here:",value=1)

    if st.button("Solve the system"):
        coeff_matrix=np.array([
            [a,b],
            [d,e]
        ])

        const=np.array([c,f])
        if np.linalg.det(coeff_matrix)==0:
            st.write("The equation has no unique solutions")

        else:
            soln=solve(coeff_matrix,const)
            st.write(f"The value of x is {soln[0]} and y is: {soln[1]}")
