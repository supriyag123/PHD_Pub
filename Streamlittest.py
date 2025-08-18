{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/supriyag123/PHD_Pub/blob/main/Streamlittest.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "T-BJGPTX7XS5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "da71b2ac-af1b-4ecc-c3fe-77b3b04c3346",
        "collapsed": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.48.1-py3-none-any.whl.metadata (9.5 kB)\n",
            "Collecting pyngrok\n",
            "  Downloading pyngrok-7.3.0-py3-none-any.whl.metadata (8.1 kB)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.2.1)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (25.0)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.5)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.14.1)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m2.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.45)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.11/dist-packages (from pyngrok) (6.0.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.1.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.3)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.8.3)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.4.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.48.1-py3-none-any.whl (9.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.9/9.9 MB\u001b[0m \u001b[31m55.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pyngrok-7.3.0-py3-none-any.whl (25 kB)\n",
            "Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m61.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m6.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pyngrok, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 pyngrok-7.3.0 streamlit-1.48.1 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit pyngrok"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile streamlit_app.py\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import datetime as dt\n",
        "import time\n",
        "\n",
        "# --- Settings ---\n",
        "SENSOR_COUNT = 5\n",
        "THRESHOLD = 70\n",
        "\n",
        "# --- Generate Dummy Data ---\n",
        "def create_dummy_df(n=200, anomaly_prob=0.05, seed=42):\n",
        "    np.random.seed(seed)\n",
        "    ts = [dt.datetime.now() + dt.timedelta(seconds=i) for i in range(n)]\n",
        "    data = {}\n",
        "    for i in range(1, SENSOR_COUNT + 1):\n",
        "        base = np.random.normal(50, 5, n)\n",
        "        mask = np.random.rand(n) < anomaly_prob\n",
        "        base[mask] += np.random.normal(20, 5, mask.sum())  # anomalies\n",
        "        data[f\"sensor_{i}\"] = base\n",
        "    df = pd.DataFrame(data)\n",
        "    df.insert(0, \"timestamp\", ts)\n",
        "    return df\n",
        "\n",
        "# --- UI Setup ---\n",
        "st.set_page_config(layout=\"wide\")\n",
        "\n",
        "st.title(\"🛰️ Real-Time Industrial IoT Sensor Dashboard\")\n",
        "st.markdown(\"\"\"\n",
        "Welcome to the **Simulated IoT Monitoring App**.\n",
        "\n",
        "🔹 Simulates real-time sensor readings\n",
        "🔹 Displays streaming line charts & anomalies\n",
        "🔹 Shows agent-style reasoning for detected events\n",
        "\"\"\")\n",
        "\n",
        "# --- Sidebar Controls ---\n",
        "st.sidebar.title(\"⚙️ Controls\")\n",
        "speed = st.sidebar.slider(\"⏩ Playback speed\", 0.1, 5.0, 1.0)\n",
        "window = st.sidebar.slider(\"🕓 Window size (sec)\", 5, 60, 20)\n",
        "st.sidebar.markdown(\"---\")\n",
        "st.sidebar.markdown(\"👤 Built by [Your Name](https://example.com)\")\n",
        "st.sidebar.image(\"https://upload.wikimedia.org/wikipedia/commons/4/44/Industrial_icon.png\", width=150)\n",
        "\n",
        "# --- Load Data ---\n",
        "df = create_dummy_df()\n",
        "sensor_cols = df.columns[1:]\n",
        "selected_sensors = st.multiselect(\"📊 Select sensors to display\", sensor_cols.tolist(), default=sensor_cols[:3])\n",
        "\n",
        "# --- App Layout ---\n",
        "alert = st.empty()\n",
        "chart = st.empty()\n",
        "metrics = st.columns(len(selected_sensors))\n",
        "agent_box = st.container()\n",
        "\n",
        "# --- Streaming Loop ---\n",
        "for i in range(len(df)):\n",
        "    now = df['timestamp'].iloc[i]\n",
        "    window_df = df[df['timestamp'] >= now - pd.Timedelta(seconds=window)]\n",
        "\n",
        "    # --- Chart Update ---\n",
        "    with chart.container():\n",
        "        st.line_chart(window_df.set_index(\"timestamp\")[selected_sensors])\n",
        "\n",
        "    # --- Real-Time Metrics ---\n",
        "    for j, sensor in enumerate(selected_sensors):\n",
        "        latest_val = window_df[sensor].iloc[-1]\n",
        "        metrics[j].metric(sensor, round(latest_val, 2))\n",
        "\n",
        "    # --- Anomaly Check ---\n",
        "    anomalies = (window_df[selected_sensors] > THRESHOLD).any(axis=1)\n",
        "    if anomalies.any():\n",
        "        alert.warning(\"⚠️ Anomaly detected in the selected window!\")\n",
        "        agent_message = \"Agent: Sudden spike detected. Recommend checking affected sensors.\"\n",
        "    else:\n",
        "        alert.success(\"✅ System operating normally.\")\n",
        "        agent_message = \"Agent: All sensor values within expected range.\"\n",
        "\n",
        "    # --- Agent Reasoning Panel ---\n",
        "    with agent_box:\n",
        "        st.markdown(\"### 🤖 Agent Reasoning\")\n",
        "        st.info(agent_message)\n",
        "\n",
        "    time.sleep(1.0 / speed)\n"
      ],
      "metadata": {
        "id": "oOHjAhnZs1Az",
        "outputId": "c8146296-af2e-4cef-e6b2-1fa92549af2a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing streamlit_app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run streamlit_app.py &>/dev/null&"
      ],
      "metadata": {
        "id": "eC8pcMYYaUtE"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok\n",
        "ngrok.kill()  # clean old tunnels\n",
        "\n",
        "# ⬇️ paste your token between the quotes\n",
        "ngrok.set_auth_token(\"30zHX6xv0Aqb6STXjMtLNsaa6el_45Xmu5rKv77UofrqjgkFR\")\n",
        "\n",
        "public_url = ngrok.connect(8501)  # tip: region option possible e.g. options={\"region\":\"au\"}\n",
        "print(\"Streamlit URL:\", public_url)"
      ],
      "metadata": {
        "id": "3K4QCcqas-qL",
        "outputId": "9598bc11-460d-4ed8-b8a9-7b860264f872",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Streamlit URL: NgrokTunnel: \"https://0303d33937dc.ngrok-free.app\" -> \"http://localhost:8501\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "W-RMQkgLak9I"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "Xp-Mv3Ksamxv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "0zEUESMBM_Eo"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bQ6ZgIvrdRNp"
      },
      "source": [
        "# New Section"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!jupyter nbconvert --to script Streamlittest.ipynb"
      ],
      "metadata": {
        "id": "f9yp_w6Vd10G",
        "outputId": "edcae66c-d8b8-443e-8f41-fc619881d80d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[NbConvertApp] WARNING | pattern 'Streamlittest.ipynb' matched no files\n",
            "This application is used to convert notebook files (*.ipynb)\n",
            "        to various other formats.\n",
            "\n",
            "        WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.\n",
            "\n",
            "Options\n",
            "=======\n",
            "The options below are convenience aliases to configurable class-options,\n",
            "as listed in the \"Equivalent to\" description-line of the aliases.\n",
            "To see all configurable class-options for some <cmd>, use:\n",
            "    <cmd> --help-all\n",
            "\n",
            "--debug\n",
            "    set log level to logging.DEBUG (maximize logging output)\n",
            "    Equivalent to: [--Application.log_level=10]\n",
            "--show-config\n",
            "    Show the application's configuration (human-readable format)\n",
            "    Equivalent to: [--Application.show_config=True]\n",
            "--show-config-json\n",
            "    Show the application's configuration (json format)\n",
            "    Equivalent to: [--Application.show_config_json=True]\n",
            "--generate-config\n",
            "    generate default config file\n",
            "    Equivalent to: [--JupyterApp.generate_config=True]\n",
            "-y\n",
            "    Answer yes to any questions instead of prompting.\n",
            "    Equivalent to: [--JupyterApp.answer_yes=True]\n",
            "--execute\n",
            "    Execute the notebook prior to export.\n",
            "    Equivalent to: [--ExecutePreprocessor.enabled=True]\n",
            "--allow-errors\n",
            "    Continue notebook execution even if one of the cells throws an error and include the error message in the cell output (the default behaviour is to abort conversion). This flag is only relevant if '--execute' was specified, too.\n",
            "    Equivalent to: [--ExecutePreprocessor.allow_errors=True]\n",
            "--stdin\n",
            "    read a single notebook file from stdin. Write the resulting notebook with default basename 'notebook.*'\n",
            "    Equivalent to: [--NbConvertApp.from_stdin=True]\n",
            "--stdout\n",
            "    Write notebook output to stdout instead of files.\n",
            "    Equivalent to: [--NbConvertApp.writer_class=StdoutWriter]\n",
            "--inplace\n",
            "    Run nbconvert in place, overwriting the existing notebook (only\n",
            "            relevant when converting to notebook format)\n",
            "    Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory=]\n",
            "--clear-output\n",
            "    Clear output of current file and save in place,\n",
            "            overwriting the existing notebook.\n",
            "    Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory= --ClearOutputPreprocessor.enabled=True]\n",
            "--coalesce-streams\n",
            "    Coalesce consecutive stdout and stderr outputs into one stream (within each cell).\n",
            "    Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory= --CoalesceStreamsPreprocessor.enabled=True]\n",
            "--no-prompt\n",
            "    Exclude input and output prompts from converted document.\n",
            "    Equivalent to: [--TemplateExporter.exclude_input_prompt=True --TemplateExporter.exclude_output_prompt=True]\n",
            "--no-input\n",
            "    Exclude input cells and output prompts from converted document.\n",
            "            This mode is ideal for generating code-free reports.\n",
            "    Equivalent to: [--TemplateExporter.exclude_output_prompt=True --TemplateExporter.exclude_input=True --TemplateExporter.exclude_input_prompt=True]\n",
            "--allow-chromium-download\n",
            "    Whether to allow downloading chromium if no suitable version is found on the system.\n",
            "    Equivalent to: [--WebPDFExporter.allow_chromium_download=True]\n",
            "--disable-chromium-sandbox\n",
            "    Disable chromium security sandbox when converting to PDF..\n",
            "    Equivalent to: [--WebPDFExporter.disable_sandbox=True]\n",
            "--show-input\n",
            "    Shows code input. This flag is only useful for dejavu users.\n",
            "    Equivalent to: [--TemplateExporter.exclude_input=False]\n",
            "--embed-images\n",
            "    Embed the images as base64 dataurls in the output. This flag is only useful for the HTML/WebPDF/Slides exports.\n",
            "    Equivalent to: [--HTMLExporter.embed_images=True]\n",
            "--sanitize-html\n",
            "    Whether the HTML in Markdown cells and cell outputs should be sanitized..\n",
            "    Equivalent to: [--HTMLExporter.sanitize_html=True]\n",
            "--log-level=<Enum>\n",
            "    Set the log level by value or name.\n",
            "    Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']\n",
            "    Default: 30\n",
            "    Equivalent to: [--Application.log_level]\n",
            "--config=<Unicode>\n",
            "    Full path of a config file.\n",
            "    Default: ''\n",
            "    Equivalent to: [--JupyterApp.config_file]\n",
            "--to=<Unicode>\n",
            "    The export format to be used, either one of the built-in formats\n",
            "            ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', 'slides', 'webpdf']\n",
            "            or a dotted object name that represents the import path for an\n",
            "            ``Exporter`` class\n",
            "    Default: ''\n",
            "    Equivalent to: [--NbConvertApp.export_format]\n",
            "--template=<Unicode>\n",
            "    Name of the template to use\n",
            "    Default: ''\n",
            "    Equivalent to: [--TemplateExporter.template_name]\n",
            "--template-file=<Unicode>\n",
            "    Name of the template file to use\n",
            "    Default: None\n",
            "    Equivalent to: [--TemplateExporter.template_file]\n",
            "--theme=<Unicode>\n",
            "    Template specific theme(e.g. the name of a JupyterLab CSS theme distributed\n",
            "    as prebuilt extension for the lab template)\n",
            "    Default: 'light'\n",
            "    Equivalent to: [--HTMLExporter.theme]\n",
            "--sanitize_html=<Bool>\n",
            "    Whether the HTML in Markdown cells and cell outputs should be sanitized.This\n",
            "    should be set to True by nbviewer or similar tools.\n",
            "    Default: False\n",
            "    Equivalent to: [--HTMLExporter.sanitize_html]\n",
            "--writer=<DottedObjectName>\n",
            "    Writer class used to write the\n",
            "                                        results of the conversion\n",
            "    Default: 'FilesWriter'\n",
            "    Equivalent to: [--NbConvertApp.writer_class]\n",
            "--post=<DottedOrNone>\n",
            "    PostProcessor class used to write the\n",
            "                                        results of the conversion\n",
            "    Default: ''\n",
            "    Equivalent to: [--NbConvertApp.postprocessor_class]\n",
            "--output=<Unicode>\n",
            "    Overwrite base name use for output files.\n",
            "                Supports pattern replacements '{notebook_name}'.\n",
            "    Default: '{notebook_name}'\n",
            "    Equivalent to: [--NbConvertApp.output_base]\n",
            "--output-dir=<Unicode>\n",
            "    Directory to write output(s) to. Defaults\n",
            "                                  to output to the directory of each notebook. To recover\n",
            "                                  previous default behaviour (outputting to the current\n",
            "                                  working directory) use . as the flag value.\n",
            "    Default: ''\n",
            "    Equivalent to: [--FilesWriter.build_directory]\n",
            "--reveal-prefix=<Unicode>\n",
            "    The URL prefix for reveal.js (version 3.x).\n",
            "            This defaults to the reveal CDN, but can be any url pointing to a copy\n",
            "            of reveal.js.\n",
            "            For speaker notes to work, this must be a relative path to a local\n",
            "            copy of reveal.js: e.g., \"reveal.js\".\n",
            "            If a relative path is given, it must be a subdirectory of the\n",
            "            current directory (from which the server is run).\n",
            "            See the usage documentation\n",
            "            (https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-slideshow)\n",
            "            for more details.\n",
            "    Default: ''\n",
            "    Equivalent to: [--SlidesExporter.reveal_url_prefix]\n",
            "--nbformat=<Enum>\n",
            "    The nbformat version to write.\n",
            "            Use this to downgrade notebooks.\n",
            "    Choices: any of [1, 2, 3, 4]\n",
            "    Default: 4\n",
            "    Equivalent to: [--NotebookExporter.nbformat_version]\n",
            "\n",
            "Examples\n",
            "--------\n",
            "\n",
            "    The simplest way to use nbconvert is\n",
            "\n",
            "            > jupyter nbconvert mynotebook.ipynb --to html\n",
            "\n",
            "            Options include ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', 'slides', 'webpdf'].\n",
            "\n",
            "            > jupyter nbconvert --to latex mynotebook.ipynb\n",
            "\n",
            "            Both HTML and LaTeX support multiple output templates. LaTeX includes\n",
            "            'base', 'article' and 'report'.  HTML includes 'basic', 'lab' and\n",
            "            'classic'. You can specify the flavor of the format used.\n",
            "\n",
            "            > jupyter nbconvert --to html --template lab mynotebook.ipynb\n",
            "\n",
            "            You can also pipe the output to stdout, rather than a file\n",
            "\n",
            "            > jupyter nbconvert mynotebook.ipynb --stdout\n",
            "\n",
            "            PDF is generated via latex\n",
            "\n",
            "            > jupyter nbconvert mynotebook.ipynb --to pdf\n",
            "\n",
            "            You can get (and serve) a Reveal.js-powered slideshow\n",
            "\n",
            "            > jupyter nbconvert myslides.ipynb --to slides --post serve\n",
            "\n",
            "            Multiple notebooks can be given at the command line in a couple of\n",
            "            different ways:\n",
            "\n",
            "            > jupyter nbconvert notebook*.ipynb\n",
            "            > jupyter nbconvert notebook1.ipynb notebook2.ipynb\n",
            "\n",
            "            or you can specify the notebooks list in a config file, containing::\n",
            "\n",
            "                c.NbConvertApp.notebooks = [\"my_notebook.ipynb\"]\n",
            "\n",
            "            > jupyter nbconvert --config mycfg.py\n",
            "\n",
            "To see all available configurables, use `--help-all`.\n",
            "\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "machine_shape": "hm",
      "mount_file_id": "https://github.com/supriyag123/PHD_Pub/blob/main/PAPER_GDRNet_METROPM_Step1.ipynb",
      "authorship_tag": "ABX9TyO+VRuR5wTxntdXeeQzbd8Q",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}