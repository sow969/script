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
#         # df = df.dropna(axis=1, how='all')  # Peut être activé si besoin

#         st.success("✅ Fichier chargé avec succès !")
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
#                 .str.replace(r"[^\d.,\-]", "", regex=True)  # Conserve chiffres, virgules, points, et -
#                 .str.replace(",", "", regex=False)          # Supprime séparateurs de milliers
#             )

#             # Conversion en nombre et suppression des signes négatifs
#             df["Montant"] = pd.to_numeric(df["Montant"], errors='coerce')
#             df["Montant"] = df["Montant"].abs()

#             # ➕ Regrouper les descriptions "Sortie cheque..."
#             df["Type Description"] = df["Description"].apply(
#                 lambda x: "Sortie cheque" if isinstance(x, str) and x.strip().lower().startswith("sortie cheque") else x
#             )

#             st.markdown("---")
#             st.subheader("📁 Les types de transactions :")

#             groupes = df.groupby("Type Description")

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

# import streamlit as st
# import pandas as pd
# import io

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
#         # df = df.dropna(axis=1, how='all')  # Peut être activé si besoin

#         st.success("✅ Fichier chargé avec succès !")
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
#                 .str.replace(r"[^\d.,\-]", "", regex=True)  # Conserve chiffres, virgules, points, et -
#                 .str.replace(",", "", regex=False)          # Supprime séparateurs de milliers
#             )

#             # Conversion en nombre et suppression des signes négatifs
#             df["Montant"] = pd.to_numeric(df["Montant"], errors='coerce')
#             df["Montant"] = df["Montant"].abs()

#             # ➕ Regrouper les descriptions "Sortie cheque..."
#             df["Type Description"] = df["Description"].apply(
#                 lambda x: "Sortie cheque" if isinstance(x, str) and x.strip().lower().startswith("sortie cheque") else x
#             )

#             st.markdown("---")
#             st.subheader("📁 Les types de transactions :")

#             groupes = df.groupby("Type Description")

#             # Préparation du tableau final pour l'affichage
#             df_groupes_final = []

#             for description, group_df in groupes:
#                 somme_solde = group_df["Montant"].sum(skipna=True)
#                 lignes = len(group_df)

#                 with st.expander(f"📌 `{description}`", expanded=False):
#                     st.markdown(f"**💰 Somme : `{somme_solde:,.2f}` MGA**")
#                     st.write("Nombres de lignes:", lignes)
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

#                 # Création de la ligne de total
#                 ligne_total = pd.DataFrame([{col: "" for col in group_df.columns}])
#                 ligne_total.iloc[0]["Description"] = f"Total {description}"
#                 ligne_total.iloc[0]["Montant"] = f"{somme_solde:,.2f}"

#                 # Ajouter le groupe + sa ligne de total
#                 group_complet = pd.concat([group_df.drop(columns=["Type Description"]), ligne_total], ignore_index=True)
#                 df_groupes_final.append(group_complet)

#             # Fusion de tous les groupes pour afficher le tableau final
#             df_final = pd.concat(df_groupes_final, ignore_index=True)
            
#             # Affichage du tableau final avec tous les groupes et les totaux
#             st.markdown("---")
#             st.subheader("📊 Fichier final apres traitement:")
#             st.dataframe(df_final, use_container_width=True)
#             st.write("Nombres de lignes:", len(df_final))

#             # Total général
#             total_general = df["Montant"].sum(skipna=True)
#             st.markdown("---")
#             st.success(f"🧾 **Total général de tous les montants : `{total_general:,.2f}` MGA**")

#             # Télécharger le fichier complet avec les totaux
#             buffer_final = io.StringIO()
#             df_final.to_csv(buffer_final, index=False)
#             st.download_button(
#                 label="📥 Télécharger le fichier",
#                 data=buffer_final.getvalue(),
#                 file_name="lot-mada.csv",
#                 mime="text/csv",
#                 use_container_width=True
#             )

#         else:
#             st.error("❌ Le fichier doit contenir les colonnes 'Description' et 'Montant'.")

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

#         st.success("✅ Fichier chargé avec succès !")
#         with st.expander("🔎 Aperçu du fichier traité", expanded=False):
#             st.dataframe(df, use_container_width=True)

#         # Vérifie la présence des colonnes nécessaires
#         if "Description" in df.columns and "Montant" in df.columns:

#             # Nettoyage avancé de la colonne Montant
#             df["Montant"] = df["Montant"].astype(str)
#             df["Montant"] = df["Montant"].str.replace(r"^([0-9.,]+)-$", r"-\1", regex=True)
#             df["Montant"] = (
#                 df["Montant"]
#                 .str.replace(r"[^\d.,\-]", "", regex=True)
#                 .str.replace(",", "", regex=False)
#             )
#             df["Montant"] = pd.to_numeric(df["Montant"], errors='coerce')
#             df["Montant"] = df["Montant"].abs()

#             # ➕ Regrouper les descriptions "Sortie cheque..."
#             df["Type Description"] = df["Description"].apply(
#                 lambda x: "Sortie cheque" if isinstance(x, str) and x.strip().lower().startswith("sortie cheque") else x
#             )

#             st.markdown("---")
#             st.subheader("📁 Les types de transactions :")

#             groupes = df.groupby("Type Description")
#             df_groupes_final = []

#             for description, group_df in groupes:
#                 somme_solde = group_df["Montant"].sum(skipna=True)
#                 lignes = len(group_df)

#                 with st.expander(f"📌 `{description}`", expanded=False):
#                     st.markdown(f"**💰 Somme : `{somme_solde:,.2f}` MGA**")
#                     st.write("Nombres de lignes: ", lignes)
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

#                 # Créer la ligne de total avec le nombre de lignes affiché dans la description
#                 ligne_total = pd.DataFrame([{col: "" for col in group_df.columns}])
#                 ligne_total.iloc[0]["Description"] = f"Total {description} ({lignes} lignes)"
#                 ligne_total.iloc[0]["Montant"] = f"{somme_solde:,.2f}"
#                 ligne_total.iloc[0]["Type Description"] = description  # Conserver pour structure cohérente

#                 # Ajouter le groupe + sa ligne de total
#                 group_complet = pd.concat([group_df, ligne_total], ignore_index=True)
#                 df_groupes_final.append(group_complet)

#             # Fusion de tous les groupes
#             df_final = pd.concat(df_groupes_final, ignore_index=True)

#             # Affichage du tableau final avec tous les groupes et les totaux
#             st.markdown("---")
#             st.subheader("📊 Fichier final après traitement :")
#             st.dataframe(df_final, use_container_width=True)
#             st.write("Nombres de lignes:", len(df_final))

#             # Total général
#             total_general = df["Montant"].sum(skipna=True)
#             st.markdown("---")
#             st.success(f"🧾 **Total général de tous les montants : `{total_general:,.2f}` MGA**")

#             # Télécharger le fichier complet avec les totaux
#             buffer_final = io.StringIO()
#             df_final.to_csv(buffer_final, index=False)
#             st.download_button(
#                 label="📥 Télécharger le fichier",
#                 data=buffer_final.getvalue(),
#                 file_name="lot-mada.csv",
#                 mime="text/csv",
#                 use_container_width=True
#             )

#         else:
#             st.error("❌ Le fichier doit contenir les colonnes 'Description' et 'Montant'.")

#     except Exception as e:
#         st.error(f"❌ Une erreur est survenue lors du traitement du fichier : {e}")
# else:
#     st.info("🕐 En attente du téléversement d'un fichier CSV.")


# import streamlit as st
# st.set_page_config(page_title="🔍 LOT MADA - Multi PDF", layout="wide")

# import pandas as pd
# import io
# from PIL import Image
# import fitz  # PyMuPDF
# import re

# # === Style CSS personnalisé ===
# st.markdown("""
# <style>
# h1, h2, h3 {
#     color: #D63384;
# }
# .metric-label {
#     font-weight: bold;
#     color: #6f42c1;
# }
# .metric-value {
#     font-weight: bold;
#     color: #198754;
#     font-size: 18px;
# }
# div[data-testid="metric-container"] {
#     background-color: #fff0f6;
#     border-radius: 0.5rem;
#     padding: 0.5rem;
#     margin-bottom: 1rem;
# }
# hr {
#     border-top: 2px solid #D63384;
# }
# </style>
# """, unsafe_allow_html=True)

# # Fonction pour extraire les mots de valeur : "10- VIREMENT", etc.
# def extract_keywords(text):
#     pattern = r"\d+-\s*([A-Za-z\s]+)"
#     return re.findall(pattern, text)

# # Titre principal
# st.markdown("<h1 style='color: #D63384;'>Traitement de Fichiers - Lot MADA</h1>", unsafe_allow_html=True)
# st.markdown("<hr>", unsafe_allow_html=True)

# # === SIDEBAR ===
# with st.sidebar:
#     logo = Image.open("logo.png")
#     st.image(logo, width=80)
#     st.subheader("📤 Téléversement")

#     uploaded_file_csv = st.file_uploader("CSV - Relevé de transactions", type="csv")
#     uploaded_files_pdf = st.file_uploader("PDF - Televersement", type="pdf", accept_multiple_files=True)

# # === TRAITEMENT PRINCIPAL ===
# if uploaded_file_csv and uploaded_files_pdf:
#     try:
#         df_csv = pd.read_csv(uploaded_file_csv, skiprows=4)
#         df_csv.columns = df_csv.columns.str.strip()

#         if "Description" in df_csv.columns and "Montant" in df_csv.columns:

#             # Nettoyage du montant
#             df_csv["Montant"] = (
#                 df_csv["Montant"]
#                 .astype(str)
#                 .str.replace(r"^([0-9.,]+)-$", r"-\1", regex=True)
#                 .str.replace(r"[^\d.,\-]", "", regex=True)
#                 .str.replace(",", "")
#             )
#             df_csv["Montant"] = pd.to_numeric(df_csv["Montant"], errors='coerce').abs()

#             # Identification des types
#             df_csv["Type Description"] = df_csv["Description"].apply(
#                 lambda x: "Sortie cheque" if isinstance(x, str) and x.lower().startswith("sortie cheque") else x
#             )

#             groupes = df_csv.groupby("Type Description")
#             groupes_list = list(groupes)

#             st.subheader("📁 Types de Transactions")
#             df_groupes_final = []

#             for description, group_df in groupes_list:
#                 somme = group_df["Montant"].sum()
#                 lignes = len(group_df)

#                 with st.expander(f"📌 `{description}`", expanded=False):
#                     col1, col2 = st.columns(2)
#                     col1.markdown(f"<span class='metric-label' style='color: #D63384;'>Nombre de lignes</span>", unsafe_allow_html=True)
#                     col1.markdown(f"<div class='metric-value'>{lignes}</div>", unsafe_allow_html=True)

#                     col2.markdown(f"<span class='metric-label' style='color: #D63384;'>Total MGA</span>", unsafe_allow_html=True)
#                     col2.markdown(f"<div class='metric-value'>{somme:,.2f}</div>", unsafe_allow_html=True)

#                     st.dataframe(group_df, use_container_width=True)

#                     buffer = io.StringIO()
#                     group_df.to_csv(buffer, index=False)
#                     st.download_button("📥 Télécharger", buffer.getvalue(), f"{description}.csv", mime='text/csv')

#                 # Total ligne
#                 ligne_total = pd.DataFrame([{col: "" for col in group_df.columns}])
#                 ligne_total.at[0, "Description"] = f"Total {description} ({lignes} lignes)"
#                 ligne_total.at[0, "Montant"] = f"{somme:,.2f}"
#                 ligne_total.at[0, "Type Description"] = description

#                 df_groupes_final.append(pd.concat([group_df, ligne_total], ignore_index=True))

#             # Fichier final
#             df_final_csv = pd.concat(df_groupes_final, ignore_index=True)
#             st.subheader("📊 Fichier final")
#             st.dataframe(df_final_csv, use_container_width=True)

#             total_general = df_csv['Montant'].sum()
#             st.success(f"🧾 Total général (CSV) : `{total_general:,.2f}` MGA")

#             # Téléchargement
#             buffer_final_csv = io.StringIO()
#             df_final_csv.to_csv(buffer_final_csv, index=False)
#             st.download_button("📥 Télécharger tout le fichier", buffer_final_csv.getvalue(), "lot-mada.csv", mime="text/csv")

#             # ========== PDF PROCESSING ==========
#             st.markdown("---")
#             all_pdf_data = []

#             for uploaded_pdf in uploaded_files_pdf:
#                 try:
#                     doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
#                     if len(doc) >= 2:
#                         text = doc.load_page(1).get_text()
#                         doc.close()

#                         marker = "SITUATION DEFINITIVE DU PARTICIPANT BAOBAB BANQUE MADAGASCAR"
#                         if marker in text:
#                             portion = text.split(marker, 1)[-1]
#                             cleaned = portion.replace(",", "").replace("\xa0", " ")

#                             keywords = extract_keywords(cleaned)
#                             matches = re.findall(r"\d+(?: \d{3})*\.\d{2}|\b\d+\b", cleaned)

#                             values = []
#                             for m in matches:
#                                 try:
#                                     val = float(m.replace(" ", ""))
#                                     values.append(val)
#                                 except:
#                                     continue

#                             nbres_lignes = int(values[10]) if len(values) > 10 else None
#                             montant = float(values[11]) if len(values) > 11 else None

#                             valeur_match = re.search(r"Valeur\s*:\s*(.+)", text)
#                             valeur_extrait = valeur_match.group(1).strip() if valeur_match else "Non trouvé"
#                             valpdf = extract_keywords(valeur_extrait)

#                             # Comparaison avec le CSV
#                             for description, group_df in groupes_list:
#                                 if valpdf and any(valpdf[0].lower() in str(desc).lower() for desc in group_df["Description"]):
#                                     csv_lignes = len(group_df)
#                                     csv_montant = group_df["Montant"].sum()

#                                     all_pdf_data.append({
#                                         "Fichier PDF": uploaded_pdf.name,
#                                         "Transactions": description,
#                                         "Lignes PDF": nbres_lignes,
#                                         "Lignes CSV": csv_lignes,
#                                         "Écart Lignes": nbres_lignes - csv_lignes if nbres_lignes is not None else "❓",
#                                         "Montant PDF": montant,
#                                         "Montant CSV": csv_montant,
#                                         "Écart Montant": montant - csv_montant if montant is not None else "❓",
#                                         "Valeur PDF": valeur_extrait
#                                     })
#                     else:
#                         st.error(f"❌ Le PDF {uploaded_pdf.name} n'a pas assez de pages.")
#                 except Exception as e:
#                     st.error(f"❌ Erreur dans {uploaded_pdf.name} : {e}")

#             if all_pdf_data:
#                 df_pdf_results = pd.DataFrame(all_pdf_data)
#                 st.subheader("📊 Résumé Comparaison PDF / CSV")
#                 st.dataframe(df_pdf_results, use_container_width=True)

#                 buffer_pdf = io.StringIO()
#                 df_pdf_results.to_csv(buffer_pdf, index=False)
#                 st.download_button("📥 Télécharger la comparaison CSV/PDF", buffer_pdf.getvalue(), "comparaison_csv_pdf.csv", mime="text/csv")
#             else:
#                 st.warning("📄 Aucun PDF traité avec succès.")
#         else:
#             st.error("❌ Le fichier CSV doit contenir les colonnes 'Description' et 'Montant'.")
#     except Exception as e:
#         st.error(f"❌ Erreur de traitement : {e}")
# else:
#     st.info("📂 Veuillez importer un fichier CSV et au moins un PDF.")
import streamlit as st
st.set_page_config(page_title="LOT MADA", layout="wide")

import pandas as pd
import io
from PIL import Image
import fitz  # PyMuPDF
import re

# === Style CSS personnalisé ===
st.markdown("""
<style>
h1, h2, h3 {
    color: #D63384;
}
.metric-label {
    font-weight: bold;
    color: #6f42c1;
}
.metric-value {
    font-weight: bold;
    color: #198754;
    font-size: 18px;
}
div[data-testid="metric-container"] {
    background-color: #fff0f6;
    border-radius: 0.5rem;
    padding: 0.5rem;
    margin-bottom: 1rem;
}
hr {
    border-top: 2px solid #D63384;
}
</style>
""", unsafe_allow_html=True)


# Fonction de style pour le DataFrame PDF/CSV
def style_dataframe(df):
    def color_diff(val):
        if isinstance(val, (int, float)):
            if val < 0:
                color = 'red'
            elif val > 0:
                color = 'green'
            else:
                color = 'black'
        else:
            color = 'black'
        return f'color: {color}; font-weight: bold;'

    styled = df.style.applymap(color_diff, subset=['Écart Lignes', 'Écart Montant']) \
                    .format({
                    'Montant PDF': '{:,.2f}',
                    'Montant CSV': '{:,.2f}',
                    'Écart Montant': '{:,.2f}'
                    }) \
                    .set_properties(**{'text-align': 'center'}) \
                    .set_table_styles([
                    {'selector': 'th', 'props': [('background-color', '#D63384'), ('color', 'white'), ('text-align', 'center')]},
                    {'selector': 'td', 'props': [('padding', '8px')]}
])
    return styled

# Fonction pour extraire les mots de valeur : "10- VIREMENT", etc.
def extract_keywords(text):
    pattern = r"\d+-\s*([A-Za-z\s]+)"
    return re.findall(pattern, text)

# Titre principal
st.markdown("<h1 style='color: #D63384;'>Traitement de Fichiers - Lot MADA</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# === SIDEBAR ===
with st.sidebar:
    logo = Image.open("logo.png")
    st.image(logo, width=80)
    st.subheader("📤 Téléversement")

    uploaded_file_csv = st.file_uploader("CSV - Relevé de transactions", type="csv")
    uploaded_files_pdf = st.file_uploader("PDF - Televersement", type="pdf", accept_multiple_files=True)

# === TRAITEMENT PRINCIPAL ===
if uploaded_file_csv and uploaded_files_pdf:
    try:
        df_csv = pd.read_csv(uploaded_file_csv, skiprows=4)
        df_csv.columns = df_csv.columns.str.strip()

        if "Description" in df_csv.columns and "Montant" in df_csv.columns:

            # Nettoyage du montant
            df_csv["Montant"] = (
                df_csv["Montant"]
                .astype(str)
                .str.replace(r"^([0-9.,]+)-$", r"-\1", regex=True)
                .str.replace(r"[^\d.,\-]", "", regex=True)
                .str.replace(",", "")
            )
            df_csv["Montant"] = pd.to_numeric(df_csv["Montant"], errors='coerce').abs()

            # Identification des types
            df_csv["Type Description"] = df_csv["Description"].apply(
                lambda x: "Sortie cheque" if isinstance(x, str) and x.lower().startswith("sortie cheque") else x
            )

            groupes = df_csv.groupby("Type Description")
            groupes_list = list(groupes)

            st.subheader("📁 Types de Transactions")
            df_groupes_final = []

            for description, group_df in groupes_list:
                somme = group_df["Montant"].sum()
                lignes = len(group_df)

                with st.expander(f"📌 `{description}`", expanded=False):
                    col1, col2 = st.columns(2)
                    col1.markdown(f"<span class='metric-label' style='color: #D63384;'>Nombre de lignes</span>", unsafe_allow_html=True)
                    col1.markdown(f"<div class='metric-value'>{lignes}</div>", unsafe_allow_html=True)

                    col2.markdown(f"<span class='metric-label' style='color: #D63384;'>Total MGA</span>", unsafe_allow_html=True)
                    col2.markdown(f"<div class='metric-value'>{somme:,.2f}</div>", unsafe_allow_html=True)

                    st.dataframe(group_df, use_container_width=True)

                    buffer = io.StringIO()
                    group_df.to_csv(buffer, index=False)
                    st.download_button("📥 Télécharger", buffer.getvalue(), f"{description}.csv", mime='text/csv')

                # Total ligne
                ligne_total = pd.DataFrame([{col: "" for col in group_df.columns}])
                ligne_total.at[0, "Description"] = f"Total {description} ({lignes} lignes)"
                ligne_total.at[0, "Montant"] = f"{somme:,.2f}"
                ligne_total.at[0, "Type Description"] = description

                df_groupes_final.append(pd.concat([group_df, ligne_total], ignore_index=True))

            # Fichier final
            df_final_csv = pd.concat(df_groupes_final, ignore_index=True)
            st.subheader("📊 Fichier final")
            st.dataframe(df_final_csv, use_container_width=True)

            total_general = df_csv['Montant'].sum()
            st.success(f"🧾 Total général (CSV) : `{total_general:,.2f}` MGA")

            # Téléchargement
            buffer_final_csv = io.StringIO()
            df_final_csv.to_csv(buffer_final_csv, index=False)
            st.download_button("📥 Télécharger tout le fichier", buffer_final_csv.getvalue(), "lot-mada.csv", mime="text/csv")

            # ========== PDF PROCESSING ==========
            st.markdown("---")
            all_pdf_data = []

            for uploaded_pdf in uploaded_files_pdf:
                if uploaded_pdf.name == '10.21.pdf':
                    try:
                        doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
                        if len(doc) >= 2:
                            text = doc.load_page(1).get_text()
                            doc.close()

                            marker = "SITUATION DEFINITIVE DU PARTICIPANT BAOBAB BANQUE MADAGASCAR"
                            if marker in text:
                                portion = text.split(marker, 1)[-1]
                                cleaned = portion.replace(",", "").replace("\xa0", " ")

                                keywords = extract_keywords(cleaned)
                                matches = re.findall(r"\d+(?: \d{3})*\.\d{2}|\b\d+\b", cleaned)

                                values = []
                                for m in matches:
                                    try:
                                        val = float(m.replace(" ", ""))
                                        values.append(val)
                                    except:
                                        continue

                                # Extraction selon indices
                                nbres_virement = int(values[10]) if len(values) > 10 else None
                                montant_virement = float(values[11]) if len(values) > 11 else None

                                nbres_interbank = int(values[15]) if len(values) > 15 else None
                                montant_interbank = float(values[16]) if len(values) > 16 else None
                                

                                valeur_match = re.search(r"Valeur\s*:\s*(.+)", text)
                                valeur_extrait = valeur_match.group(1).strip() if valeur_match else "Non trouvé"
                                valpdf = extract_keywords(valeur_extrait)
                                
                                # Liste des transactions à comparer
                                transactions_pdf = [
                                    {"type": "VIREMENT", "nbres": nbres_virement, "montant": montant_virement},
                                    {"type": "INWARD INTERBANK TRANSFER", "nbres": nbres_interbank, "montant": montant_interbank}
                                ]
                                

                                # Comparaison avec le CSV
                                for tx in transactions_pdf:
                                    for description, group_df in groupes_list:
                                        # Vérifie si la description CSV contient le type PDF
                                        if tx["type"].lower() in str(description).lower():
                                            csv_lignes = len(group_df)
                                            csv_montant = group_df["Montant"].sum()

                                            all_pdf_data.append({
                                                "Fichier PDF": uploaded_pdf.name,
                                                "Transactions": tx["type"],
                                                "Lignes Bank": tx["nbres"],
                                                "Lignes Baobab": csv_lignes,
                                                "Écart Lignes": tx["nbres"] - csv_lignes if tx["nbres"] is not None else "❓",
                                                "Montant Bank": tx["montant"],
                                                "Montant Baobab": csv_montant,
                                                "Écart Montant": tx["montant"] - csv_montant if tx["montant"] is not None else "❓",
                                                "Valeur PDF": valeur_extrait
                                            })
                        else:
                            st.error(f"❌ Le PDF {uploaded_pdf.name} n'a pas assez de pages.")
                    except Exception as e:
                        st.error(f"❌ Erreur dans {uploaded_pdf.name} : {e}")
            
                elif uploaded_pdf.name == '30.21.pdf':
                    try:
                        doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
                        if len(doc) >= 2:
                            text = doc.load_page(1).get_text()
                            doc.close()

                            marker = "SITUATION DEFINITIVE DU PARTICIPANT BAOBAB BANQUE MADAGASCAR"
                            if marker in text:
                                portion = text.split(marker, 1)[-1]
                                cleaned = portion.replace(",", "").replace("\xa0", " ")

                                keywords = extract_keywords(cleaned)
                                matches = re.findall(r"\d+(?: \d{3})*\.\d{2}|\b\d+\b", cleaned)

                                values = []
                                for m in matches:
                                    try:
                                        val = float(m.replace(" ", ""))
                                        values.append(val)
                                    except:
                                        continue

                                nbres_inwardchequefromclear = int(values[10]) if len(values) > 10 else None
                                montant_inwardchequefromclear = float(values[11]) if len(values) > 11 else None
                                
                                nbres_Outwardcheque = int(values[15]) if len(values) > 15 else None
                                montant_Outwardcheque = int(values[16]) if len(values) > 16 else None
                                
                                nbres_returncheques = int(values[12]) if len(values) > 12 else None
                                montant_returncheques = int(values[13]) if len(values) > 13 else None
                                
                                

                                valeur_match = re.search(r"Valeur\s*:\s*(.+)", text)
                                valeur_extrait = valeur_match.group(1).strip() if valeur_match else "Non trouvé"
                                valpdf = extract_keywords(valeur_extrait)
                                
                                # Liste des transactions à comparer
                                transactions_pdf = [
                                    {"type": "Inward Cheques from Clearing", 
                                    "nbres": nbres_inwardchequefromclear, 
                                    "montant": montant_inwardchequefromclear},
                                    {"type": "Outward cheque Susp. DR", 
                                    "nbres": nbres_Outwardcheque,
                                    "montant": montant_Outwardcheque},
                                    {"type": "Returned Cheques from Clearing", 
                                    "nbres": nbres_returncheques,
                                    "montant": montant_returncheques}
                                ]

                                # Comparaison avec le CSV
                                # Comparaison avec le CSV
                                for tx in transactions_pdf:
                                    for description, group_df in groupes_list:
                                        # Vérifie si la description CSV contient le type PDF
                                        if tx["type"].lower() in str(description).lower():
                                            csv_lignes = len(group_df)
                                            csv_montant = group_df["Montant"].sum()

                                            all_pdf_data.append({
                                                "Fichier PDF": uploaded_pdf.name,
                                                "Transactions": tx["type"],
                                                "Lignes Bank": tx["nbres"],
                                                "Lignes Baobab": csv_lignes,
                                                "Écart Lignes": tx["nbres"] - csv_lignes if tx["nbres"] is not None else "❓",
                                                "Montant Bank": tx["montant"],
                                                "Montant Baobab": csv_montant,
                                                "Écart Montant": tx["montant"] - csv_montant if tx["montant"] is not None else "❓",
                                                "Valeur PDF": valeur_extrait
                                            })
                        else:
                            st.error(f"❌ Le PDF {uploaded_pdf.name} n'a pas assez de pages.")
                    except Exception as e:
                        st.error(f"❌ Erreur dans {uploaded_pdf.name} : {e}")
                    
                        
                elif uploaded_pdf.name == '40.21.pdf':
                    try:
                        doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
                        if len(doc) >= 2:
                            text = doc.load_page(1).get_text()
                            doc.close()
                            

                            marker = "SITUATION DEFINITIVE DU PARTICIPANT BAOBAB BANQUE MADAGASCAR"
                            if marker in text:
                                portion = text.split(marker, 1)[-1]
                                cleaned = portion.replace(",", "").replace("\xa0", " ")
                                

                                keywords = extract_keywords(cleaned)
                                matches = re.findall(r"\d+(?: \d{3})*\.\d{2}|\b\d+\b", cleaned)

                                values = []
                                for m in matches:
                                    try:
                                        val = float(m.replace(" ", ""))
                                        values.append(val)
                                    except:
                                        continue

                                nbres_lignesEntreeEffetDr = int(values[10]) if len(values) > 10 else None
                                montantEntreeEffetDr = float(values[11]) if len(values) > 11 else None
                                
                                nbres_sortieeffet = int(values[15]) if len(values) > 15 else None
                                montant_sortieeffet = int(values[16]) if len(values) > 16 else None
                                

                                valeur_match = re.search(r"Valeur\s*:\s*(.+)", text)
                                valeur_extrait = valeur_match.group(1).strip() if valeur_match else "Non trouvé"
                                valpdf = extract_keywords(valeur_extrait)
                                
                                # Liste des transactions à comparer
                                transactions_pdf = [
                                    {"type": "Entree Effet -Dr", "nbres": nbres_lignesEntreeEffetDr, "montant": montantEntreeEffetDr},
                                    {"type": "Sortie Effet -Cr", "nbres": nbres_sortieeffet, "montant": montant_sortieeffet}
                                ]

                                # Comparaison avec le CSV
                                for tx in transactions_pdf:
                                    for description, group_df in groupes_list:
                                        # Vérifie si la description CSV contient le type PDF
                                        if tx["type"].lower() in str(description).lower():
                                            csv_lignes = len(group_df)
                                            csv_montant = group_df["Montant"].sum()

                                            all_pdf_data.append({
                                                "Fichier PDF": uploaded_pdf.name,
                                                "Transactions": tx["type"],
                                                "Lignes Bank": tx["nbres"],
                                                "Lignes Baobab": csv_lignes,
                                                "Écart Lignes": tx["nbres"] - csv_lignes if tx["nbres"] is not None else "❓",
                                                "Montant Bank": tx["montant"],
                                                "Montant Baobab": csv_montant,
                                                "Écart Montant": tx["montant"] - csv_montant if tx["montant"] is not None else "❓",
                                                "Valeur PDF": valeur_extrait
                                            })
                        else:
                            st.error(f"❌ Le PDF {uploaded_pdf.name} n'a pas assez de pages.")
                    except Exception as e:
                        st.error(f"❌ Erreur dans {uploaded_pdf.name} : {e}")
            if all_pdf_data:
                df_pdf_results = pd.DataFrame(all_pdf_data)
                st.subheader("📊 Résumé Comparaison PDF / CSV")
                st.dataframe(style_dataframe(df_pdf_results), use_container_width=True)

                buffer_pdf = io.StringIO()
                df_pdf_results.to_csv(buffer_pdf, index=False)
                st.download_button("📥 Télécharger la comparaison CSV/PDF", buffer_pdf.getvalue(), "comparaison_csv_pdf.csv", mime="text/csv")
            else:
                st.warning("📄 Aucun PDF traité avec succès.")
        else:
            st.error("❌ Le fichier CSV doit contenir les colonnes 'Description' et 'Montant'.")
    except Exception as e:
        st.error(f"❌ Erreur de traitement : {e}")
else:
    st.info("📂 Veuillez importer un fichier CSV et au moins un PDF.")



