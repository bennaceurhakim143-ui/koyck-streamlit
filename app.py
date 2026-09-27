import streamlit as st
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Économétrie Dynamique - Modèle de Koyck",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 34px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    .subtitle {
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">'
    '📊 Économétrie Dynamique'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='text-align:center;'>"
    "Modèles à retards distribués : Modèle de Koyck"
    "</h2>",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📚 Navigation")

section = st.sidebar.radio(
    "Choisir une section :",
    [
        "🏠 Accueil",
        "📚 Cours théorique",
        "📐 Transformation de Koyck",
        "🧮 Exemple numérique",
        "🎲 Simulation",
        "📊 Estimation",
        "📈 Analyse dynamique",
        "📝 Exercices"
    ]
)


# ============================================================
# ACCUEIL
# ============================================================

if section == "🏠 Accueil":

    st.header("Bienvenue")

    st.markdown(
        """
        Cette application accompagne le cours d'**Économétrie Dynamique**
        consacré aux **modèles à retards distribués** et particulièrement
        au **modèle de Koyck**.

        L'application permet de :

        - comprendre la formulation du modèle ;
        - effectuer la transformation de Koyck ;
        - simuler des données ;
        - estimer le modèle par MCO ;
        - calculer les multiplicateurs de court et long terme ;
        - calculer le retard moyen ;
        - analyser la vitesse d'ajustement ;
        - réaliser des exercices interactifs.
        """
    )

    st.info(
        """
        Objectif pédagogique :

        Passer progressivement de la théorie économique à
        l'estimation économétrique et à l'interprétation des résultats.
        """
    )

    st.markdown("### Modèle de Koyck")

    st.latex(
        r"""
        Y_t =
        \alpha+
        \beta_0X_t+
        \beta_0\lambda X_{t-1}+
        \beta_0\lambda^2X_{t-2}+\cdots+
        \varepsilon_t
        """
    )


# ============================================================
# COURS THEORIQUE
# ============================================================

elif section == "📚 Cours théorique":

    st.header("1. Modèle à retards distribués")

    st.markdown(
        """
        Dans de nombreux phénomènes économiques, l'effet d'une variable
        explicative sur la variable dépendante ne se produit pas
        instantanément.

        Une variation de l'investissement, de la consommation publique,
        du revenu ou d'une autre variable économique peut produire des
        effets qui se prolongent pendant plusieurs périodes.
        """
    )

    st.latex(
        r"""
        Y_t =
        \alpha+
        \beta_0X_t+
        \beta_1X_{t-1}+
        \beta_2X_{t-2}+\cdots+
        \varepsilon_t
        """
    )

    st.markdown("### Hypothèse de Koyck")

    st.markdown(
        """
        Koyck suppose que les coefficients des retards suivent
        une progression géométrique décroissante.
        """
    )

    st.latex(
        r"""
        \beta_j=\beta_0\lambda^j
        """
    )

    st.latex(
        r"""
        0<\lambda<1
        """
    )

    st.markdown("Le modèle devient alors :")

    st.latex(
        r"""
        Y_t =
        \alpha+
        \beta_0X_t+
        \beta_0\lambda X_{t-1}+
        \beta_0\lambda^2X_{t-2}+\cdots+
        \varepsilon_t
        """
    )

    st.success(
        "Lorsque λ est proche de 1, l'effet de X se prolonge davantage dans le temps."
    )


# ============================================================
# TRANSFORMATION DE KOYCK
# ============================================================

elif section == "📐 Transformation de Koyck":

    st.header("2. Transformation de Koyck")

    st.markdown("Le modèle initial est :")

    st.latex(
        r"""
        Y_t =
        \alpha+
        \beta_0X_t+
        \beta_0\lambda X_{t-1}+
        \beta_0\lambda^2X_{t-2}+\cdots+
        \varepsilon_t
        """
    )

    st.markdown("À la période précédente :")

    st.latex(
        r"""
        Y_{t-1} =
        \alpha+
        \beta_0X_{t-1}+
        \beta_0\lambda X_{t-2}+
        \cdots+
        \varepsilon_{t-1}
        """
    )

    st.markdown("En multipliant la deuxième équation par λ :")

    st.latex(
        r"""
        \lambda Y_{t-1}
        =
        \lambda\alpha+
        \beta_0\lambda X_{t-1}+
        \beta_0\lambda^2X_{t-2}+\cdots+
        \lambda\varepsilon_{t-1}
        """
    )

    st.markdown("Après soustraction :")

    st.latex(
        r"""
        Y_t-\lambda Y_{t-1}
        =
        \alpha(1-\lambda)
        +
        \beta_0X_t
        +
        v_t
        """
    )

    st.latex(
        r"""
        v_t=\varepsilon_t-\lambda\varepsilon_{t-1}
        """
    )

    st.success("Forme économétrique estimable :")

    st.latex(
        r"""
        \boxed{
        Y_t=c+\beta_0X_t+\lambda Y_{t-1}+v_t
        }
        """
    )

    st.latex(
        r"""
        c=\alpha(1-\lambda)
        """
    )


# ============================================================
# EXEMPLE NUMERIQUE
# ============================================================

elif section == "🧮 Exemple numérique":

    st.header("3. Exemple numérique")

    st.markdown("Considérons le modèle estimé :")

    st.latex(
        r"""
        Y_t=10+0.40X_t+0.60Y_{t-1}+u_t
        """
    )

    beta = 0.40
    lam = 0.60

    short_run = beta

    long_run = beta / (1 - lam)

    mean_lag = lam / (1 - lam)

    speed = 1 - lam

    half_life = np.log(0.5) / np.log(lam)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Multiplicateur court terme",
            f"{short_run:.4f}"
        )

    with c2:
        st.metric(
            "Multiplicateur long terme",
            f"{long_run:.4f}"
        )

    with c3:
        st.metric(
            "Retard moyen",
            f"{mean_lag:.4f}"
        )

    with c4:
        st.metric(
            "Vitesse d'ajustement",
            f"{speed:.4f}"
        )

    st.markdown("### Coefficients des retards")

    lags = np.arange(0, 10)

    coefficients = beta * lam ** lags

    lag_df = pd.DataFrame(
        {
            "Retard": lags,
            "Coefficient": coefficients
        }
    )

    st.dataframe(
        lag_df,
        use_container_width=True
    )

    fig, ax = plt.subplots()

    ax.bar(
        lags,
        coefficients
    )

    ax.set_xlabel("Retard")
    ax.set_ylabel("Coefficient")
    ax.set_title("Décroissance des coefficients de Koyck")

    st.pyplot(fig)

    st.metric(
        "Demi-vie de l'effet",
        f"{half_life:.4f}"
    )


# ============================================================
# SIMULATION
# ============================================================

elif section == "🎲 Simulation":

    st.header("4. Simulation d'un modèle de Koyck")

    st.sidebar.subheader("Paramètres")

    n = st.sidebar.slider(
        "Taille de l'échantillon",
        min_value=50,
        max_value=1000,
        value=200
    )

    alpha = st.sidebar.number_input(
        "α",
        value=2.0,
        step=0.1
    )

    beta = st.sidebar.number_input(
        "β₀",
        value=0.8,
        step=0.1
    )

    lam = st.sidebar.slider(
        "λ",
        min_value=0.05,
        max_value=0.95,
        value=0.60,
        step=0.01
    )

    sigma = st.sidebar.number_input(
        "Écart-type de l'erreur",
        min_value=0.1,
        value=1.0,
        step=0.1
    )

    seed = st.sidebar.number_input(
        "Seed",
        min_value=0,
        value=42
    )

    np.random.seed(int(seed))

    X = np.random.normal(
        loc=10,
        scale=2,
        size=n
    )

    epsilon = np.random.normal(
        loc=0,
        scale=sigma,
        size=n
    )

    Y = np.zeros(n)

    Y[0] = (
        alpha
        + beta * X[0]
        + epsilon[0]
    )

    for t in range(1, n):

        Y[t] = (
            alpha
            + beta * X[t]
            + lam * Y[t - 1]
            + epsilon[t]
        )

    df = pd.DataFrame(
        {
            "X": X,
            "Y": Y
        }
    )

    st.subheader("Données simulées")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    fig, ax = plt.subplots()

    ax.plot(
        df["Y"],
        label="Y"
    )

    ax.plot(
        df["X"],
        label="X"
    )

    ax.set_title(
        "Séries simulées"
    )

    ax.set_xlabel("Temps")
    ax.legend()

    st.pyplot(fig)

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Télécharger les données CSV",
        data=csv,
        file_name="koyck_simulation.csv",
        mime="text/csv"
    )


# ============================================================
# ESTIMATION
# ============================================================

elif section == "📊 Estimation":

    st.header("5. Estimation du modèle de Koyck")

    st.markdown("Le modèle estimé est :")

    st.latex(
        r"""
        Y_t=c+\beta X_t+\lambda Y_{t-1}+u_t
        """
    )

    uploaded_file = st.file_uploader(
        "Importer un fichier CSV",
        type=["csv"]
    )

    if uploaded_file is None:

        st.info(
            "Veuillez importer un fichier CSV contenant au minimum Y et X."
        )

    else:

        df = pd.read_csv(
            uploaded_file
        )

        st.subheader("Données")

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

        columns = df.columns.tolist()

        if len(columns) < 2:

            st.error(
                "Le fichier doit contenir au moins deux variables."
            )

        else:

            y_var = st.selectbox(
                "Variable dépendante Y",
                columns
            )

            x_candidates = [
                c for c in columns
                if c != y_var
            ]

            x_var = st.selectbox(
                "Variable explicative X",
                x_candidates
            )

            df["Y_lag"] = (
                df[y_var]
                .shift(1)
            )

            data = df.dropna().copy()

            X = data[
                [
                    x_var,
                    "Y_lag"
                ]
            ]

            X = sm.add_constant(X)

            y = data[y_var]

            try:

                model = sm.OLS(
                    y,
                    X
                ).fit()

                st.subheader(
                    "Résultats de l'estimation"
                )

                result_table = pd.DataFrame(
                    {
                        "Coefficient":
                            model.params,
                        "Std. Error":
                            model.bse,
                        "t-statistic":
                            model.tvalues,
                        "p-value":
                            model.pvalues
                    }
                )

                st.dataframe(
                    result_table,
                    use_container_width=True
                )

                st.subheader(
                    "Statistiques du modèle"
                )

                c1, c2, c3, c4 = st.columns(4)

                with c1:
                    st.metric(
                        "R²",
                        f"{model.rsquared:.4f}"
                    )

                with c2:
                    st.metric(
                        "R² ajusté",
                        f"{model.rsquared_adj:.4f}"
                    )

                with c3:
                    st.metric(
                        "Observations",
                        f"{int(model.nobs)}"
                    )

                with c4:
                    st.metric(
                        "F-statistic",
                        f"{model.fvalue:.4f}"
                    )

                beta_hat = model.params[x_var]

                lambda_hat = model.params["Y_lag"]

                st.subheader(
                    "Paramètres dynamiques"
                )

                if (
                    0 < lambda_hat < 1
                ):

                    short_run = beta_hat

                    long_run = (
                        beta_hat /
                        (1 - lambda_hat)
                    )

                    mean_lag = (
                        lambda_hat /
                        (1 - lambda_hat)
                    )

                    speed = (
                        1 -
                        lambda_hat
                    )

                    half_life = (
                        np.log(0.5) /
                        np.log(lambda_hat)
                    )

                    c1, c2, c3, c4 = st.columns(4)

                    with c1:
                        st.metric(
                            "Court terme",
                            f"{short_run:.4f}"
                        )

                    with c2:
                        st.metric(
                            "Long terme",
                            f"{long_run:.4f}"
                        )

                    with c3:
                        st.metric(
                            "Retard moyen",
                            f"{mean_lag:.4f}"
                        )

                    with c4:
                        st.metric(
                            "Vitesse",
                            f"{speed:.4f}"
                        )

                    st.metric(
                        "Demi-vie",
                        f"{half_life:.4f}"
                    )

                else:

                    st.warning(
                        "La valeur estimée de λ n'est pas comprise entre 0 et 1. "
                        "L'interprétation standard du modèle de Koyck "
                        "n'est donc pas applicable directement."
                    )

                st.subheader(
                    "Valeurs observées et ajustées"
                )

                data["Y_hat"] = model.predict(
                    X
                )

                fig, ax = plt.subplots()

                ax.plot(
                    data.index,
                    data[y_var],
                    label="Y observé"
                )

                ax.plot(
                    data.index,
                    data["Y_hat"],
                    label="Y estimé"
                )

                ax.set_xlabel(
                    "Temps"
                )

                ax.set_ylabel(
                    y_var
                )

                ax.legend()

                st.pyplot(fig)

                st.subheader(
                    "Résumé économétrique"
                )

                st.text(
                    model.summary().as_text()
                )

            except Exception as e:

                st.error(
                    f"Erreur lors de l'estimation : {e}"
                )


# ============================================================
# ANALYSE DYNAMIQUE
# ============================================================

elif section == "📈 Analyse dynamique":

    st.header("6. Analyse dynamique")

    beta = st.number_input(
        "Coefficient β₀",
        value=0.40,
        step=0.01
    )

    lam = st.slider(
        "Coefficient λ",
        min_value=0.01,
        max_value=0.99,
        value=0.60,
        step=0.01
    )

    short_run = beta

    long_run = (
        beta /
        (1 - lam)
    )

    mean_lag = (
        lam /
        (1 - lam)
    )

    speed = (
        1 -
        lam
    )

    half_life = (
        np.log(0.5) /
        np.log(lam)
    )

    st.subheader(
        "Indicateurs"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Multiplicateur court terme",
            f"{short_run:.4f}"
        )

        st.latex(
            r"""
            M_{SR}=\beta_0
            """
        )

    with c2:

        st.metric(
            "Multiplicateur long terme",
            f"{long_run:.4f}"
        )

        st.latex(
            r"""
            M_{LR}=\frac{\beta_0}{1-\lambda}
            """
        )

    c3, c4 = st.columns(2)

    with c3:

        st.metric(
            "Retard moyen",
            f"{mean_lag:.4f}"
        )

        st.latex(
            r"""
            L=\frac{\lambda}{1-\lambda}
            """
        )

    with c4:

        st.metric(
            "Vitesse d'ajustement",
            f"{speed:.4f}"
        )

        st.latex(
            r"""
            S=1-\lambda
            """
        )

    st.metric(
        "Demi-vie",
        f"{half_life:.4f}"
    )

    st.latex(
        r"""
        h=\frac{\ln(0.5)}{\ln(\lambda)}
        """
    )

    st.subheader(
        "Décroissance des effets dans le temps"
    )

    max_lag = st.slider(
        "Nombre de périodes",
        min_value=3,
        max_value=30,
        value=10
    )

    lags = np.arange(
        max_lag
    )

    effects = (
        beta *
        lam ** lags
    )

    effect_df = pd.DataFrame(
        {
            "Retard": lags,
            "Effet": effects
        }
    )

    st.dataframe(
        effect_df,
        use_container_width=True
    )

    fig, ax = plt.subplots()

    ax.bar(
        lags,
        effects
    )

    ax.set_xlabel(
        "Retard"
    )

    ax.set_ylabel(
        "Effet marginal"
    )

    ax.set_title(
        "Distribution temporelle de l'effet"
    )

    st.pyplot(fig)


# ============================================================
# EXERCICES
# ============================================================

elif section == "📝 Exercices":

    st.header("7. Exercices")

    st.markdown(
        """
        ### Exercice 1

        On considère le modèle :

        """
    )

    st.latex(
        r"""
        Y_t=5+0.30X_t+0.70Y_{t-1}+u_t
        """
    )

    st.markdown(
        """
        Calculer :

        1. Le multiplicateur de court terme.
        2. Le multiplicateur de long terme.
        3. Le retard moyen.
        4. La vitesse d'ajustement.
        """
    )

    st.markdown(
        "### Votre réponse pour le multiplicateur de long terme"
    )

    answer = st.number_input(
        "Valeur",
        value=0.0,
        step=0.01
    )

    if st.button(
        "✅ Vérifier"
    ):

        correct = (
            0.30 /
            (1 - 0.70)
        )

        if abs(
            answer - correct
        ) < 0.01:

            st.success(
                "Bonne réponse ! ✅"
            )

        else:

            st.error(
                f"Réponse incorrecte. "
                f"La valeur correcte est {correct:.2f}."
            )

    st.markdown("---")

    st.markdown(
        """
        ### Exercice 2

        Supposons que :

        """
    )

    st.latex(
        r"""
        \beta_0=0.50
        \quad\text{et}\quad
        \lambda=0.80
        """
    )

    st.markdown(
        """
        Calculer :

        - le multiplicateur de court terme ;
        - le multiplicateur de long terme ;
        - le retard moyen ;
        - la vitesse d'ajustement.
        """
    )

    show_answer = st.checkbox(
        "Afficher la correction"
    )

    if show_answer:

        st.latex(
            r"""
            M_{SR}=0.50
            """
        )

        st.latex(
            r"""
            M_{LR}=
            \frac{0.50}{1-0.80}
            =2.50
            """
        )

        st.latex(
            r"""
            L=
            \frac{0.80}{1-0.80}
            =4
            """
        )

        st.latex(
            r"""
            S=1-0.80=0.20
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.sidebar.markdown("---")

st.sidebar.caption(
    "Économétrie Dynamique — Modèle de Koyck"
)

st.sidebar.caption(
    "Application pédagogique"
)