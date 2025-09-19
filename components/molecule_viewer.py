import streamlit.components.v1 as components
import py3Dmol

def show_molecule(composition):
    if not composition:
        return

    for molecule in composition:
        st_mol = py3Dmol.view(width=400, height=300)

        if molecule == "CH4":
            st_mol.addModel("C", "sdf")
        elif molecule == "H2O":
            st_mol.addModel("O", "sdf")
        elif molecule == "CO2":
            st_mol.addModel("O=C=O", "xyz")
        else:
            continue

        st_mol.setStyle({'stick': {}})
        st_mol.zoomTo()

        # ✅ Ensure HTML is a string
        html = st_mol._make_html()  # Use internal method to get HTML string
        components.html(html, height=300)

# import streamlit.components.v1 as components
# import py3Dmol

# def show_molecule(composition):
#     if not composition:
#         return

#     st_mol = py3Dmol.view(width=400, height=300)
#     for molecule in composition:
#         if molecule == "CH4":
#             st_mol.addModel("C", "sdf")  # Methane
#         elif molecule == "H2O":
#             st_mol.addModel("O", "sdf")  # Water
#         elif molecule == "CO2":
#             st_mol.addModel("O=C=O", "xyz")  # Carbon dioxide
#         else:
#             continue
#         st_mol.setStyle({'stick': {}})
#         st_mol.zoomTo()
#         html = st_mol.render().replace('"', '&quot;')
#         components.html(html, height=300)
