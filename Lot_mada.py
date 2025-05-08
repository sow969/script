# import streamlit as st
# import pandas as pd
# import io

# # Configuration de la page
# st.set_page_config(page_title="🔍 LOT MADA", layout="wide")
# st.markdown(
#     "<h1 style='text-align: center; color: #4B8BBE;'>🔍 Traitement de Fichiers - Lot MADA</h1>", 
#     unsafe_allow_html=True
# )

# st.markdown("---")

# # Zone de téléversement du fichier
# with st.container():
#     st.subheader("📤 Téléversement du fichier CSV")
#     uploaded_file = st.file_uploader("Sélectionne un fichier CSV contenant les données à traiter :", type="csv")

# # Traitement du fichier une fois téléversé
# if uploaded_file is not None:
#     try:
#         df = pd.read_csv(uploaded_file, skiprows=5, delimiter=',')
#         df.columns = df.columns.str.strip()
#         df = df.dropna(axis=1, how='all')

#         st.success("✅ Fichier chargé et colonnes vides supprimées avec succès !")
        
#         with st.expander("🔎 Aperçu du fichier traité (colonnes nettoyées)", expanded=False):
#             st.dataframe(df, use_container_width=True)

#         if "Description" in df.columns:
#             st.markdown("---")
#             st.subheader("📁 Groupes générés par la colonne 'Description'")

#             groupes = dict(tuple(df.groupby("Description")))

#             for description, group_df in groupes.items():
#                 with st.expander(f"📌`{description}`", expanded=False):
#                     st.dataframe(group_df, use_container_width=True)

#                     buffer = io.StringIO()
#                     group_df.to_csv(buffer, index=False)
#                     st.download_button(
#                         label="📥 Télécharger ce groupe",
#                         data=buffer.getvalue(),
#                         file_name=f"{description.replace('/', '_')}.csv",
#                         mime='text/csv',
#                         use_container_width=True
#                     )
#         else:
#             st.error("❌ La colonne 'Description' est introuvable dans le fichier. Veuillez vérifier le contenu.")
#     except Exception as e:
#         st.error(f"❌ Une erreur est survenue lors du traitement du fichier : {e}")
# else:
#     st.info("🕐 En attente du téléversement d'un fichier CSV pour démarrer le traitement.")


# import streamlit as st
# import pandas as pd
# import io

# st.set_page_config(page_title="🔍 LOT MADA", layout="wide")
# st.markdown(
#     "<h1 style='text-align: center; color: #4B8BBE;'>🔍 Traitement de Fichiers - Lot MADA</h1>", 
#     unsafe_allow_html=True
# )
# st.markdown("---")

# with st.container():
#     st.subheader("📤 Téléversement du fichier CSV")
#     uploaded_file = st.file_uploader("Sélectionne un fichier CSV contenant les données à traiter :", type="csv")

# if uploaded_file is not None:
#     try:
#         df = pd.read_csv(uploaded_file, skiprows=5, delimiter=',')

#         # Nettoyage
#         df.columns = df.columns.str.strip()
#         df = df.dropna(axis=1, how='all')

#         # Conversion de la colonne 'Solde' en numérique
#         if "Credit" in df.columns:
#             df["Credit"] = pd.to_numeric(df["Credit"], errors='coerce')

#         st.success("✅ Fichier chargé et colonnes vides supprimées avec succès !")
#         with st.expander("🔎 Aperçu du fichier traité", expanded=False):
#             st.dataframe(df, use_container_width=True)

#         if "Description" in df.columns:
#             st.markdown("---")
#             st.subheader("📁 Groupes générés par la colonne 'Description'")

#             groupes = dict(tuple(df.groupby("Description")))

#             for description, group_df in groupes.items():
#                 somme_solde = group_df["Credit"].sum()

#                 with st.expander(f"📌`{description}`", expanded=False):
#                     st.markdown(f"**💰 Somme: `{somme_solde:,.2f}` MGA**")
#                     st.dataframe(group_df, use_container_width=True)

#                     buffer = io.StringIO()
#                     group_df.to_csv(buffer, index=False)
#                     st.download_button(
#                         label="📥 Télécharger ce groupe",
#                         data=buffer.getvalue(),
#                         file_name=f"{description.replace('/', '_')}.csv",
#                         mime='text/csv',
#                         use_container_width=True
#                     )
#         else:
#             st.error("❌ La colonne 'Description' est introuvable dans le fichier. Veuillez vérifier le contenu.")
#     except Exception as e:
#         st.error(f"❌ Une erreur est survenue lors du traitement du fichier : {e}")
# else:
#     st.info("🕐 En attente du téléversement d'un fichier CSV pour démarrer le traitement.")




# import streamlit as st
# import pandas as pd
# import io

# st.set_page_config(page_title="🔍 LOT MADA", layout="wide")
# st.markdown(
#     "<h1 style='text-align: center; color: #4B8BBE;'>🔍 Traitement de Fichiers - Lot MADA</h1>", 
#     unsafe_allow_html=True
# )
# st.markdown("---")

# with st.container():
#     st.subheader("📤 Téléversement du fichier CSV")
#     uploaded_file = st.file_uploader("Sélectionne un fichier CSV contenant les données à traiter :", type="csv")

# if uploaded_file is not None:
#     try:
#         df = pd.read_csv(uploaded_file, skiprows=5, delimiter=',')
        
#         # Nettoyage
#         df.columns = df.columns.str.strip()
#         df = df.dropna(axis=1, how='all')

#         st.success("✅ Fichier chargé avec succès!")
#         with st.expander("🔎 Aperçu du fichier traité", expanded=False):
#             st.dataframe(df, use_container_width=True)

#         if "Description" in df.columns:
#             st.markdown("---")
#             st.subheader("📁 Les types de transactions:")

#             groupes = dict(tuple(df.groupby("Description")))

#             for description, group_df in groupes.items():
#                 # Nettoyage des colonnes
#                 if "Debit" in group_df.columns:
#                     group_df["Debit"] = group_df["Debit"].astype(str).str.replace("'", "", regex=False)
#                     group_df["Debit"] = pd.to_numeric(group_df["Debit"], errors='coerce')

#                 if "Credit" in group_df.columns:
#                     group_df["Credit"] = pd.to_numeric(group_df["Credit"], errors='coerce')

#                 # Calcul du solde selon la priorité
#                 somme_solde = 0
#                 type_montant = "Aucun"

#                 if group_df["Credit"].notna().any() and (group_df["Credit"] != 0).any():
#                     somme_solde = group_df["Credit"].sum()
#                     type_montant = "Credit"
#                 elif group_df["Debit"].notna().any() and (group_df["Debit"] != 0).any():
#                     somme_solde = group_df["Debit"].sum()
#                     type_montant = "Debit"

#                 # Affichage
#                 with st.expander(f"📌`{description}`", expanded=False):
#                     st.markdown(f"**💰 Somme ({type_montant}) : `{somme_solde:,.2f}` MGA**")
#                     st.dataframe(group_df, use_container_width=True)

#                     buffer = io.StringIO()
#                     group_df.to_csv(buffer, index=False)
#                     st.download_button(
#                         label="📥 Télécharger ce groupe",
#                         data=buffer.getvalue(),
#                         file_name=f"{description.replace('/', '_')}.csv",
#                         mime='text/csv',
#                         use_container_width=True
#                     )
#         else:
#             st.error("❌ La colonne 'Description' est introuvable dans le fichier.")
#     except Exception as e:
#         st.error(f"❌ Une erreur est survenue lors du traitement du fichier : {e}")
# else:
#     st.info("🕐 En attente du téléversement d'un fichier CSV.")


# import streamlit as st
# import pandas as pd
# import io

# # Configuration de la page
# st.set_page_config(page_title="🔍 LOT MADA", layout="wide")
# st.markdown(
#     "<h1 style='text-align: center; color: #4B8BBE;'>🔍 Traitement de Fichiers - Lot MADA</h1>", 
#     unsafe_allow_html=True
# )
# st.markdown("---")

# # Téléversement du fichier
# with st.container():
#     st.subheader("📤 Téléversement du fichier CSV")
#     uploaded_file = st.file_uploader("Sélectionne un fichier CSV contenant les données à traiter :", type="csv")

# # Traitement après le téléversement
# if uploaded_file is not None:
#     try:
#         # Lecture du fichier CSV (saut de 4 lignes si en-têtes inutiles)
#         df = pd.read_csv(uploaded_file, skiprows=4, delimiter=',')

#         # Nettoyage des colonnes
#         df.columns = df.columns.str.strip()
#         df = df.dropna(axis=1, how='all')

#         st.success("✅ Fichier chargé et colonnes vides supprimées avec succès !")
#         with st.expander("🔎 Aperçu du fichier traité", expanded=False):
#             st.dataframe(df, use_container_width=True)

#         # Vérifie la présence des colonnes nécessaires
#         if "Description" in df.columns and "Montant" in df.columns:

#             # Nettoyage avancé de la colonne Montant
#             df["Montant"] = df["Montant"].astype(str)

#             # Gérer les formats bancaires de type "153,230-" → "-153,230"
#             df["Montant"] = df["Montant"].str.replace(r"^([0-9.,]+)-$", r"-\1", regex=True)

#             # Supprimer les caractères inutiles (MGA, espaces, etc.) et normaliser
#             df["Montant"] = (
#                 df["Montant"]
#                 .str.replace(r"[^\d.,\-]", "", regex=True)  # Conserve chiffres, virgule, point et -
#                 .str.replace(",", "", regex=False)          # Supprime séparateur de milliers
#             )

#             # Conversion finale
#             df["Montant"] = pd.to_numeric(df["Montant"], errors='coerce')
#             df["Montant"] = df["Montant"].abs()

#             st.markdown("---")
#             st.subheader("📁 Les types de transactions:")

#             groupes = df.groupby("Description")

#             for description, group_df in groupes:
#                 somme_solde = group_df["Montant"].sum(skipna=True)

#                 with st.expander(f"📌 `{description}`", expanded=False):
#                     st.markdown(f"**💰 Somme : `{somme_solde:,.2f}` MGA**")
#                     st.dataframe(group_df, use_container_width=True)

#                     buffer = io.StringIO()
#                     group_df.to_csv(buffer, index=False)
#                     st.download_button(
#                         label="📥 Télécharger ce groupe",
#                         data=buffer.getvalue(),
#                         file_name=f"{description.replace('/', '_')}.csv",
#                         mime='text/csv',
#                         use_container_width=True
#                     )

#             # Total général
#             total_general = df["Montant"].sum(skipna=True)
#             st.markdown("---")
#             st.success(f"🧾 **Total général de tous les montants : `{total_general:,.2f}` MGA**")

#         else:
#             st.error("❌ Le fichier doit contenir les colonnes 'Description' et 'Montant'.")

#     except Exception as e:
#         st.error(f"❌ Une erreur est survenue lors du traitement du fichier : {e}")
# else:
#     st.info("🕐 En attente du téléversement d'un fichier CSV.")

import streamlit as st
import pandas as pd
import io

# Configuration de la page
st.set_page_config(page_title="🔍 LOT MADA", layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>🔍 Traitement de Fichiers - Lot MADA</h1>", 
    unsafe_allow_html=True
)
st.markdown("---")

# Téléversement du fichier
with st.container():
    st.subheader("📤 Téléversement du fichier CSV")
    uploaded_file = st.file_uploader("Sélectionne un fichier CSV contenant les données à traiter :", type="csv")

# Traitement après le téléversement
if uploaded_file is not None:
    try:
        # Lecture du fichier CSV (saut de 4 lignes si en-têtes inutiles)
        df = pd.read_csv(uploaded_file, skiprows=4, delimiter=',')

        # Nettoyage des colonnes
        df.columns = df.columns.str.strip()
        # df = df.dropna(axis=1, how='all')  # Peut être activé si besoin

        st.success("✅ Fichier chargé avec succès !")
        with st.expander("🔎 Aperçu du fichier traité", expanded=False):
            st.dataframe(df, use_container_width=True)

        # Vérifie la présence des colonnes nécessaires
        if "Description" in df.columns and "Montant" in df.columns:

            # Nettoyage avancé de la colonne Montant
            df["Montant"] = df["Montant"].astype(str)

            # Gérer les formats bancaires de type "153,230-" → "-153,230"
            df["Montant"] = df["Montant"].str.replace(r"^([0-9.,]+)-$", r"-\1", regex=True)

            # Supprimer les caractères inutiles (MGA, espaces, etc.) et normaliser
            df["Montant"] = (
                df["Montant"]
                .str.replace(r"[^\d.,\-]", "", regex=True)  # Conserve chiffres, virgules, points, et -
                .str.replace(",", "", regex=False)          # Supprime séparateurs de milliers
            )

            # Conversion en nombre et suppression des signes négatifs
            df["Montant"] = pd.to_numeric(df["Montant"], errors='coerce')
            df["Montant"] = df["Montant"].abs()

            # ➕ Regrouper les descriptions "Sortie cheque..."
            df["Type Description"] = df["Description"].apply(
                lambda x: "Sortie cheque" if isinstance(x, str) and x.strip().lower().startswith("sortie cheque") else x
            )

            st.markdown("---")
            st.subheader("📁 Les types de transactions :")

            groupes = df.groupby("Type Description")

            for description, group_df in groupes:
                somme_solde = group_df["Montant"].sum(skipna=True)

                with st.expander(f"📌 `{description}`", expanded=False):
                    st.markdown(f"**💰 Somme : `{somme_solde:,.2f}` MGA**")
                    st.dataframe(group_df, use_container_width=True)

                    buffer = io.StringIO()
                    group_df.to_csv(buffer, index=False)
                    st.download_button(
                        label="📥 Télécharger ce groupe",
                        data=buffer.getvalue(),
                        file_name=f"{description.replace('/', '_')}.csv",
                        mime='text/csv',
                        use_container_width=True
                    )

            # Total général
            total_general = df["Montant"].sum(skipna=True)
            st.markdown("---")
            st.success(f"🧾 **Total général de tous les montants : `{total_general:,.2f}` MGA**")

        else:
            st.error("❌ Le fichier doit contenir les colonnes 'Description' et 'Montant'.")

    except Exception as e:
        st.error(f"❌ Une erreur est survenue lors du traitement du fichier : {e}")
else:
    st.info("🕐 En attente du téléversement d'un fichier CSV.")

