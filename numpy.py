import streamlit as st
import numpy as np

def main():
    st.title('NumPy Tutorial: From Basics to Advanced')
    st.write("""
    Welcome to the interactive NumPy tutorial. NumPy is a powerful library for numerical computing in Python.
    This tutorial covers essential NumPy concepts and advanced features.
    """)

    # Basic operations section
    st.header('1. Basics of NumPy')
    st.write("""
    ### 1.1 Array Creation
    Create NumPy arrays using `np.array()`:
    ```python
    import numpy as np
    arr1d = np.array([1, 2, 3, 4, 5])
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    ```
    """)
    
    # Display basic array creation example
    show_basic_array_creation()

    # Slicing and indexing section
    st.header('2. Indexing and Slicing')
    st.write("""
    ### 2.1 Indexing
    Indexing in NumPy arrays is 0-based:
    ```python
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(arr[0])  # 1
    ```
    ### 2.2 Slicing
    Slice arrays to get subsets:
    ```python
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(arr[2:4])  # [3, 4]
    ```
    """)
    
    # Display indexing and slicing example
    show_indexing_slicing()

    # Broadcasting section
    st.header('3. Broadcasting')
    st.write("""
    NumPy arrays allow broadcasting:
    ```python
    import numpy as np
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([10, 20, 30])
    result = arr1 + arr2
    ```
    """)
    
    # Display broadcasting example
    show_broadcasting()

    # Universal functions (ufuncs) section
    st.header('4. Universal Functions (ufuncs)')
    st.write("""
    NumPy provides universal functions for element-wise operations:
    ```python
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    result = np.sqrt(arr)
    ```
    """)
    
    # Display ufuncs example
    show_ufuncs()

def show_basic_array_creation():
    st.code("""
    import numpy as np
    arr1d = np.array([1, 2, 3, 4, 5])
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr1d)
    print(arr2d)
    """)

def show_indexing_slicing():
    st.code("""
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(arr[0])     # 1
    print(arr[2:4])   # [3, 4]
    """)

def show_broadcasting():
    st.code("""
    import numpy as np
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([10, 20, 30])
    result = arr1 + arr2
    print(result)
    """)

def show_ufuncs():
    st.code("""
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    result = np.sqrt(arr)
    print(result)
    """)

if __name__ == '__main__':
    main()
