{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41ce92f5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73da4de2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "198ed6d0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0eb072d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Import necessary libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score\n",
    "from sklearn.preprocessing import StandardScaler, LabelEncoder\n",
    "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n",
    "import io\n",
    "import joblib\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "     \n",
    "\n",
    "# Step 1: Upload the dataset in Google Colab\n",
    "print(\"Please upload the Excel file containing the dataset.\")\n",
    "uploaded = files.upload()\n",
    "     \n",
    "\n",
    "# Load the dataset (assumes the uploaded file is an Excel file)\n",
    "file_name = list(uploaded.keys())[0]\n",
    "df = pd.read_excel(uploaded[file_name])  # Correct way to read excel\n",
    "\n",
    "     \n",
    "<ipython-input-23-ab97c54d4fca>:3: FutureWarning: Passing bytes to 'read_excel' is deprecated and will be removed in a future version. To read from a byte string, wrap it in a `BytesIO` object.\n",
    "  df = pd.read_excel(uploaded[file_name])  # Correct way to read excel\n",
    "\n",
    "# Display basic information\n",
    "print(\"\\nDataset Overview:\\n\")\n",
    "print(df.head())\n",
    "     \n",
    "\n",
    "\n",
    "# Check for null values and summary statistics\n",
    "print(\"\\nMissing Values:\\n\")\n",
    "print(df.isnull().sum())\n",
    "     \n",
    "Missing Values:\n",
    "\n",
    "movie_title              0\n",
    "movie_info              24\n",
    "critics_consensus     8329\n",
    "rating                   0\n",
    "genre                   17\n",
    "directors              114\n",
    "writers               1349\n",
    "cast                   284\n",
    "in_theaters_date       815\n",
    "on_streaming_date        2\n",
    "runtime_in_minutes     155\n",
    "studio_name            416\n",
    "tomatometer_status       0\n",
    "tomatometer_rating       0\n",
    "tomatometer_count        0\n",
    "audience_rating        252\n",
    "dtype: int64\n",
    "\n",
    "print(\"\\nStatistical Summary:\\n\")\n",
    "print(df.describe())\n",
    "\n",
    "\n",
    "# Visualize target variable distribution\n",
    "if 'audience_rating' in df.columns:\n",
    "    sns.histplot(df['audience_rating'], bins=30, kde=True)\n",
    "    plt.title('Distribution of Audience Rating')\n",
    "    plt.show()\n",
    "else:\n",
    "    raise ValueError(\"The target variable 'audience_rating' is not in the dataset.\")\n",
    "\n",
    "     \n",
    "\n",
    "# Step 3: Data Preprocessing\n",
    "# Handle missing values (e.g., drop or impute)\n",
    "df = df.dropna()  # Drop rows with missing values\n",
    "\n",
    "# Convert DateTime columns to numeric features (if any)\n",
    "datetime_cols = df.select_dtypes(include=['datetime64']).columns\n",
    "for col in datetime_cols:\n",
    "    df[col] = df[col].astype(np.int64)  # Convert to Unix timestamp (numeric format)\n",
    "\n",
    "# Encode categorical features\n",
    "label_encoders = {}\n",
    "categorical_cols = df.select_dtypes(include=['object']).columns\n",
    "for col in categorical_cols:\n",
    "    le = LabelEncoder()\n",
    "    df[col] = le.fit_transform(df[col])\n",
    "    label_encoders[col] = le\n",
    "\n",
    "# Feature-target split\n",
    "X = df.drop(columns=['audience_rating'])\n",
    "y = df['audience_rating']\n",
    "\n",
    "# Train-test split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "     \n",
    "\n",
    "# Step 3: Data Preprocessing\n",
    "# Handle missing values (e.g., drop or impute)\n",
    "df = df.dropna()  # Drop rows with missing values\n",
    "\n",
    "# Convert DateTime columns to numeric features (if any)\n",
    "#datetime_cols = df.select_dtypes(include=['datetime64']).columns #Original line\n",
    "datetime_cols = df.select_dtypes(include=['datetime64[ns]']).columns #Updated line to specify nanosecond precision\n",
    "for col in datetime_cols:\n",
    "    df[col] = df[col].astype(np.int64)  # Convert to Unix timestamp (numeric format)\n",
    "\n",
    "# Encode categorical features\n",
    "label_encoders = {}\n",
    "categorical_cols = df.select_dtypes(include=['object']).columns\n",
    "for col in categorical_cols:\n",
    "    # Check if the column contains mixed types and convert to string if necessary\n",
    "    if df[col].apply(type).nunique() > 1:  # Check for multiple types\n",
    "        df[col] = df[col].astype(str)  # Convert all values to strings\n",
    "\n",
    "    le = LabelEncoder()\n",
    "    df[col] = le.fit_transform(df[col])\n",
    "    label_encoders[col] = le\n",
    "\n",
    "# Feature-target split\n",
    "X = df.drop(columns=['audience_rating'])\n",
    "y = df['audience_rating']\n",
    "\n",
    "# Train-test split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "     \n",
    "\n",
    "# Step 4: Model Selection and Training\n",
    "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n",
    "\n",
    "# Define the models to evaluate\n",
    "models = {\n",
    "    'Linear Regression': LinearRegression(),\n",
    "    'Decision Tree': DecisionTreeRegressor(random_state=42),\n",
    "    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "}\n",
    "\n",
    "# Initialize a dictionary to store evaluation results\n",
    "evaluation_results = {}\n",
    "\n",
    "# Evaluate models\n",
    "print(\"\\nModel Performance:\")\n",
    "for name, model in models.items():\n",
    "    try:\n",
    "        # Fit the model to the training data\n",
    "        model.fit(X_train, y_train)\n",
    "\n",
    "        # Make predictions on the test set\n",
    "        y_pred = model.predict(X_test)\n",
    "\n",
    "        # Calculate the evaluation metrics\n",
    "        mae = mean_absolute_error(y_test, y_pred)\n",
    "        mse = mean_squared_error(y_test, y_pred)\n",
    "        r2 = r2_score(y_test, y_pred)\n",
    "\n",
    "        # Store the results in the dictionary\n",
    "        evaluation_results[name] = {\n",
    "            'MAE': mae,\n",
    "            'MSE': mse,\n",
    "            'R2 Score': r2\n",
    "        }\n",
    "\n",
    "        # Print the performance of each model\n",
    "        print(f\"{name} Performance:\")\n",
    "        print(f\" MAE: {mae:.4f}, MSE: {mse:.4f}, R2 Score: {r2:.4f}\\n\")\n",
    "\n",
    "    except Exception as e:\n",
    "        # Handle any errors that occur during fitting or prediction\n",
    "        print(f\"Error with model {name}: {e}\")\n",
    "\n",
    "# Optional: Show evaluation results in a DataFrame for better clarity\n",
    "evaluation_df = pd.DataFrame(evaluation_results)\n",
    "print(\"\\nModel Evaluation Summary:\")\n",
    "print(evaluation_df)\n",
    "\n",
    "     \n",
    "Model Performance:\n",
    "Linear Regression Performance:\n",
    " MAE: 15.7800, MSE: 356.6930, R2 Score: 0.0623\n",
    "\n",
    "Decision Tree Performance:\n",
    " MAE: 13.1564, MSE: 291.6124, R2 Score: 0.2334\n",
    "\n",
    "Random Forest Performance:\n",
    " MAE: 9.8543, MSE: 158.3718, R2 Score: 0.5837\n",
    "\n",
    "\n",
    "Model Evaluation Summary:\n",
    "          Linear Regression  Decision Tree  Random Forest\n",
    "MAE               15.780037      13.156373       9.854343\n",
    "MSE              356.693027     291.612352     158.371835\n",
    "R2 Score           0.062338       0.233420       0.583678\n",
    "\n",
    "# Step 5: Hyperparameter Tuning for Random Forest\n",
    "param_grid = {\n",
    "    'n_estimators': [50, 100, 150],\n",
    "    'max_depth': [None, 10, 20, 30],\n",
    "    'min_samples_split': [2, 5, 10]\n",
    "}\n",
    "     \n",
    "\n",
    "grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring='r2')\n",
    "grid_search.fit(X_train, y_train)\n",
    "\n",
    "print(\"Best Hyperparameters for Random Forest:\", grid_search.best_params_)\n",
    "     \n",
    "Best Hyperparameters for Random Forest: {'max_depth': 10, 'min_samples_split': 10, 'n_estimators': 150}\n",
    "\n",
    "# Final Model Evaluation\n",
    "best_rf = grid_search.best_estimator_\n",
    "y_pred_final = best_rf.predict(X_test)\n",
    "print(\"\\nFinal Model Performance:\")\n",
    "print(\"MAE:\", mean_absolute_error(y_test, y_pred_final))\n",
    "print(\"MSE:\", mean_squared_error(y_test, y_pred_final))\n",
    "print(\"R2 Score:\", r2_score(y_test, y_pred_final))\n",
    "     \n",
    "\n",
    "\n",
    "# Step 6: Pipeline Creation\n",
    "pipeline = Pipeline([\n",
    "    ('scaler', StandardScaler()),\n",
    "    ('model', RandomForestRegressor(**grid_search.best_params_, random_state=42))\n",
    "])\n",
    "\n",
    "pipeline.fit(X_train, y_train)\n",
    "final_predictions = pipeline.predict(X_test)\n",
    "print(\"Pipeline R2 Score:\", r2_score(y_test, final_predictions))\n",
    "     \n",
    "\n",
    "\n",
    "# Step 7: Predict 'audience_rating' for the existing data (same dataset)\n",
    "# Preprocess the same dataset for prediction (using the same preprocessing steps as for training data)\n",
    "df_preprocessed = df.copy()\n",
    "     \n",
    "\n",
    "# Step 7.1: Apply the same LabelEncoding for categorical features in the dataset\n",
    "for col in categorical_cols:\n",
    "    if col in df_preprocessed.columns:\n",
    "        # Ensure the label encoder was created during training, then apply the same transformation to the data\n",
    "        df_preprocessed[col] = label_encoders[col].transform(df_preprocessed[col])\n",
    "     \n",
    "\n",
    "# Step 7.1: Apply the same LabelEncoding for categorical features in the dataset\n",
    "for col in categorical_cols:\n",
    "    if col in df_preprocessed.columns:\n",
    "        # Instead of directly transforming, handle unseen labels\n",
    "        try:\n",
    "            df_preprocessed[col] = label_encoders[col].transform(df_preprocessed[col])\n",
    "        except ValueError as e:\n",
    "            # Handle unseen labels (e.g., assign a default value or ignore)\n",
    "            # Here, we'll replace unseen labels with a placeholder value like -1\n",
    "            unseen_mask = ~df_preprocessed[col].isin(label_encoders[col].classes_)\n",
    "            df_preprocessed.loc[unseen_mask, col] = -1\n",
    "            print(f\"Warning: Unseen labels in '{col}' replaced with -1.\")\n",
    "     \n",
    "\n",
    "# Step 7.2: Drop any remaining rows with missing values (if any) from the dataset\n",
    "df_preprocessed = df_preprocessed.dropna()\n",
    "     \n",
    "\n",
    "# Step 7.3: Ensure all features in df_preprocessed are numeric\n",
    "# Check if any column is still object or string type after encoding, which should no longer be the case\n",
    "print(df_preprocessed.dtypes)\n",
    "     \n",
    "movie_title                    int64\n",
    "movie_info                     int64\n",
    "critics_consensus              int64\n",
    "rating                         int64\n",
    "genre                          int64\n",
    "directors                      int64\n",
    "writers                        int64\n",
    "cast                           int64\n",
    "in_theaters_date               int64\n",
    "on_streaming_date              int64\n",
    "runtime_in_minutes           float64\n",
    "studio_name                    int64\n",
    "tomatometer_status             int64\n",
    "tomatometer_rating             int64\n",
    "tomatometer_count              int64\n",
    "audience_rating              float64\n",
    "predicted_audience_rating    float64\n",
    "dtype: object\n",
    "\n",
    "# Step 7.4: Use the trained pipeline to predict 'audience_rating' for the preprocessed dataset\n",
    "# Remove the target variable from the prediction data\n",
    "X_preprocessed = df_preprocessed.drop(columns=['audience_rating'])\n",
    "predictions = pipeline.predict(X_preprocessed)\n",
    "     \n",
    "\n",
    "# Step 7.5: Add predictions to the original dataframe as a new column\n",
    "df['predicted_audience_rating'] = predictions\n",
    "     \n",
    "\n",
    "# Step 7.6: Display predictions for the 'audience_rating' column in the dataset\n",
    "print(\"\\nPredicted 'audience_rating' for the existing dataset:\")\n",
    "print(df[['audience_rating', 'predicted_audience_rating']].head())\n",
    "     \n",
    "\n",
    "# Step 8: Save the Pipeline for Future Use (Optional, if you want to save the trained pipeline)\n",
    "pipeline_filename = 'audience_rating_pipeline.pkl'\n",
    "joblib.dump(pipeline, pipeline_filename)\n",
    "print(f\"Pipeline saved as {pipeline_filename}\")\n",
    "\n",
    "\n",
    "\n",
    "# Step 9: Validate Model Accuracy on Test Set (using the original data)\n",
    "print(\"\\nFinal Model Accuracy Validation (on the test set):\")\n",
    "print(\"R2 Score on Test Set:\", r2_score(y_test, final_predictions))\n",
    "print(\"MAE on Test Set:\", mean_absolute_error(y_test, final_predictions))\n",
    "print(\"MSE on Test Set:\", mean_squared_error(y_test, final_predictions))\n",
    "\n",
    "# Conclusion\n",
    "print(\"\\nProject Completed Successfully! Use the saved pipeline for future predictions.\")\n",
    "     \n",
    "\n",
    "\n",
    "Project Completed Successfully! Use the saved pipeline for future predictions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca047417",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3c9b09c",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "%matplotlib inline\n",
    "     \n",
    "\n",
    "# Assuming your data is in a file named 'Rotten_Tomatoes_Movies3.xls'\n",
    "df = pd.read_excel(\"Rotten_Tomatoes_Movies3.xls\")\n",
    "df.columns\n",
    "     \n",
    "Index(['movie_title', 'movie_info', 'critics_consensus', 'rating', 'genre',\n",
    "       'directors', 'writers', 'cast', 'in_theaters_date', 'on_streaming_date',\n",
    "       'runtime_in_minutes', 'studio_name', 'tomatometer_status',\n",
    "       'tomatometer_rating', 'tomatometer_count', 'audience_rating'],\n",
    "      dtype='object')\n",
    "\n",
    "df.isnull().sum()\n",
    "     \n",
    "\n",
    "df['in_theaters_date'] = pd.to_datetime(df['in_theaters_date'], errors='coerce')\n",
    "df['on_streaming_date'] = pd.to_datetime(df['on_streaming_date'], errors='coerce')\n",
    "\n",
    "# Fill missing numeric values with median\n",
    "df['audience_rating'].fillna(df['audience_rating'].median(), inplace=True)\n",
    "\n",
    "\n",
    "# Drop rows with missing required fields\n",
    "df.dropna(subset=['movie_title', 'rating', 'tomatometer_status', 'tomatometer_rating', 'tomatometer_count'], inplace=True)\n",
    "\n",
    "# Display the cleaned dataset\n",
    "df\n",
    "\n",
    "\n",
    "\n",
    "# Distribution of audience ratings\n",
    "sns.histplot(df['audience_rating'], bins=20, kde=True)\n",
    "plt.title('Distribution of Audience Ratings')\n",
    "plt.xlabel('Audience Rating')\n",
    "plt.ylabel('Frequency')\n",
    "plt.show()\n",
    "     \n",
    "\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score, confusion_matrix\n",
    "\n",
    "# Prepare data for modeling\n",
    "X = df[['tomatometer_rating', 'tomatometer_count', 'audience_rating']]\n",
    "y = df['tomatometer_status']\n",
    "\n",
    "# Split data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Train a Random Forest Classifier\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Make predictions\n",
    "y_pred = model.predict(X_test)\n",
    "\n",
    "# Calculate accuracy\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "accuracy\n",
    "    \n",
    "\n",
    "# Confusion matrix\n",
    "conf_matrix = confusion_matrix(y_test, y_pred)\n",
    "sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')\n",
    "plt.title('Confusion Matrix')\n",
    "plt.xlabel('Predicted')\n",
    "plt.ylabel('Actual')\n",
    "plt.show()\n",
    "     \n",
    "\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression # or from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import mean_squared_error\n",
    "\n",
    "# Prepare data for modeling\n",
    "X = df[['tomatometer_rating', 'tomatometer_count']]  # Choose relevant features\n",
    "y = df['audience_rating']\n",
    "\n",
    "# Split data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Train a Linear Regression model (or RandomForestRegressor)\n",
    "model = LinearRegression()  # Or model = RandomForestRegressor(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Make predictions\n",
    "y_pred = model.predict(X_test)\n",
    "\n",
    "# Evaluate the model\n",
    "mse = mean_squared_error(y_test, y_pred)\n",
    "\n",
    "\n",
    "print(f\"Mean Squared Error: {mse}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3f9cc15",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7517bb11",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score,confusion_matrix,classification_report\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "     \n",
    "\n",
    "file_path = \"Rotten_Tomatoes_Movies3.xls\"\n",
    "data = pd.read_excel(file_path, engine = \"xlrd\")\n",
    "     \n",
    "\n",
    "print(\"Original Dataset:\")\n",
    "print(data.dtypes)\n",
    "     \n",
    "\n",
    "datetime_cols = data.select_dtypes(include=['datetime']).columns\n",
    "print(\"\\nDatetime Columns:\", datetime_cols)\n",
    "     \n",
    "Datetime Columns: Index(['in_theaters_date', 'on_streaming_date'], dtype='object')\n",
    "\n",
    "for col in datetime_cols:\n",
    "    data[col + \"_year\"] = data[col].dt.year\n",
    "    data[col + \"_month\"] = data[col].dt.month\n",
    "    data[col + \"_day\"] = data[col].dt.day\n",
    "     \n",
    "\n",
    "data = data.drop(columns = datetime_cols)\n",
    "     \n",
    "\n",
    "for col in data.select_dtypes(include=['object']).columns:\n",
    "    data[col] = data[col].astype(str)\n",
    "     \n",
    "\n",
    "data = data.dropna()\n",
    "     \n",
    "\n",
    "label_encoder = LabelEncoder()\n",
    "for col in data.select_dtypes(include=['object']).columns:\n",
    "    data[col] = label_encoder.fit_transform(data[col])\n",
    "     \n",
    "\n",
    "def categorize_rating(rating):\n",
    "    if rating <= 5:\n",
    "        return \"Low\"\n",
    "    elif rating <= 8:\n",
    "        return \"Medium\"\n",
    "    else:\n",
    "        return \"High\"\n",
    "     \n",
    "\n",
    "data[\"audience_class\"] = data[\"audience_rating\"].apply(categorize_rating)\n",
    "     \n",
    "\n",
    "X = data.drop(columns=[\"audience_rating\", \"audience_class\"])\n",
    "y = data[\"audience_class\"]\n",
    "     \n",
    "\n",
    "print(\"Class Distribution in Training Data:\")\n",
    "print(y.value_counts())\n",
    "     \n",
    "\n",
    "from imblearn.over_sampling import SMOTE\n",
    "smote = SMOTE(random_state=42)\n",
    "X_resampled, y_resampled = smote.fit_resample(X, y)\n",
    "     \n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "     \n",
    "\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_pred = model.predict(X_test)\n",
    "     \n",
    "\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(\"\\nAccuracy Score:\", accuracy)\n",
    "\n",
    "\n",
    "conf_matrix = confusion_matrix(y_test, y_pred)\n",
    "class_report = classification_report(y_test, y_pred)\n",
    "print(\"\\nConfusion Matrix:\")\n",
    "print(conf_matrix)\n",
    "print(\"\\nClassification Report:\")\n",
    "print(class_report)\n",
    "     \n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.metrics import confusion_matrix\n",
    "     \n",
    "\n",
    "conf_matrix = confusion_matrix(y_test, y_pred)\n",
    "     \n",
    "\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.heatmap(conf_matrix, annot=True, fmt=\"d\", cmap=\"Blues\", xticklabels=[\"Low\", \"Medium\", \"High\"], yticklabels=[\"Low\", \"Medium\", \"High\"])\n",
    "plt.xlabel(\"Predicted Labels\")\n",
    "plt.ylabel(\"True Labels\")\n",
    "plt.title(\"Confusion Matrix\")\n",
    "plt.show()\n",
    "     \n",
    "\n",
    "\n",
    "importances = model.feature_importances_\n",
    "indices = X_train.columns\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.barh(indices, importances, color='lightblue')\n",
    "plt.xlabel('Importance')\n",
    "plt.ylabel('Feature')\n",
    "plt.title('Feature Importance')\n",
    "plt.show()\n",
    "     \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8a9a561",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "097a68ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Predicting 'audience_rating'\n",
    "# Importing the libraries\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.model_selection import train_test_split, GridSearchCV\n",
    "from sklearn.preprocessing import LabelEncoder, StandardScaler\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n",
    "from sklearn.pipeline import Pipeline\n",
    "import joblib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2991c646",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loading the Data:\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6dcdf29e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "428fc559",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b90ebce",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "505c2ea1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "001d2761",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Step 1: Load and Clean the Dataset\n",
    "def load_and_clean_data(file_path):\n",
    "    df = pd.read_excel(file_path)\n",
    "\n",
    "    # Handle missing values\n",
    "    df[\"audience_rating\"].fillna(df[\"audience_rating\"].median(), inplace=True)\n",
    "    df.dropna(subset=[\"movie_title\", \"rating\", \"tomatometer_status\", \"tomatometer_rating\", \"tomatometer_count\"], inplace=True)\n",
    "\n",
    "    # Convert datetime columns to numeric\n",
    "    datetime_cols = [\"in_theaters_date\", \"on_streaming_date\"]\n",
    "    for col in datetime_cols:\n",
    "        df[col] = pd.to_datetime(df[col], errors=\"coerce\")\n",
    "        df[col + \"_year\"] = df[col].dt.year\n",
    "        df[col + \"_month\"] = df[col].dt.month\n",
    "        df[col + \"_day\"] = df[col].dt.day\n",
    "    df.drop(columns=datetime_cols, inplace=True)\n",
    "\n",
    "    # Encode categorical features\n",
    "    label_encoders = {}\n",
    "    for col in df.select_dtypes(include=[\"object\"]).columns:\n",
    "        le = LabelEncoder()\n",
    "        df[col] = le.fit_transform(df[col].astype(str))\n",
    "        label_encoders[col] = le\n",
    "\n",
    "    return df, label_encoders\n",
    "\n",
    "# Step 2: Define the Target and Features\n",
    "def feature_target_split(df):\n",
    "    X = df.drop(columns=[\"audience_rating\"])\n",
    "    y = df[\"audience_rating\"]\n",
    "    return X, y\n",
    "\n",
    "# Step 3: Train and Evaluate Models\n",
    "def evaluate_models(X_train, y_train, X_test, y_test):\n",
    "    models = {\n",
    "        'Random Forest': RandomForestRegressor(random_state=42)\n",
    "    }\n",
    "\n",
    "    evaluation_results = {}\n",
    "\n",
    "    for name, model in models.items():\n",
    "        model.fit(X_train, y_train)\n",
    "        y_pred = model.predict(X_test)\n",
    "\n",
    "        mae = mean_absolute_error(y_test, y_pred)\n",
    "        mse = mean_squared_error(y_test, y_pred)\n",
    "        r2 = r2_score(y_test, y_pred)\n",
    "\n",
    "        evaluation_results[name] = {\n",
    "            'MAE': mae,\n",
    "            'MSE': mse,\n",
    "            'R2 Score': r2\n",
    "        }\n",
    "\n",
    "    return evaluation_results, models['Random Forest']\n",
    "\n",
    "# Step 4: Hyperparameter Tuning\n",
    "def tune_hyperparameters(X_train, y_train):\n",
    "    param_grid = {\n",
    "        'n_estimators': [50, 100, 150],\n",
    "        'max_depth': [None, 10, 20, 30],\n",
    "        'min_samples_split': [2, 5, 10]\n",
    "    }\n",
    "\n",
    "    grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring='r2')\n",
    "    grid_search.fit(X_train, y_train)\n",
    "    return grid_search.best_estimator_, grid_search.best_params_\n",
    "\n",
    "# Step 5: Build a Pipeline\n",
    "def build_pipeline(best_params):\n",
    "    pipeline = Pipeline([\n",
    "        ('scaler', StandardScaler()),\n",
    "        ('model', RandomForestRegressor(**best_params, random_state=42))\n",
    "    ])\n",
    "    return pipeline\n",
    "\n",
    "# Step 6: Main Execution\n",
    "if __name__ == \"__main__\":\n",
    "    file_path = \"Rotten_Tomatoes_Movies3.xls\"\n",
    "\n",
    "    # Load and preprocess the dataset\n",
    "    df, label_encoders = load_and_clean_data(file_path)\n",
    "\n",
    "    # Split the data\n",
    "    X, y = feature_target_split(df)\n",
    "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "    # Evaluate baseline models\n",
    "    evaluation_results, baseline_model = evaluate_models(X_train, y_train, X_test, y_test)\n",
    "    print(\"Baseline Model Evaluation:\")\n",
    "    print(pd.DataFrame(evaluation_results))\n",
    "\n",
    "    # Hyperparameter tuning\n",
    "    best_model, best_params = tune_hyperparameters(X_train, y_train)\n",
    "    print(\"Best Hyperparameters:\", best_params)\n",
    "\n",
    "    # Build and train the pipeline\n",
    "    pipeline = build_pipeline(best_params)\n",
    "    pipeline.fit(X_train, y_train)\n",
    "\n",
    "    # Evaluate the pipeline\n",
    "    y_pred = pipeline.predict(X_test)\n",
    "    print(\"Pipeline Performance:\")\n",
    "    print(\"R2 Score:\", r2_score(y_test, y_pred))\n",
    "    print(\"MAE:\", mean_absolute_error(y_test, y_pred))\n",
    "    print(\"MSE:\", mean_squared_error(y_test, y_pred))\n",
    "\n",
    "    # Save the pipeline\n",
    "    joblib.dump(pipeline, \"audience_rating_pipeline.pkl\")\n",
    "    print(\"Pipeline saved as audience_rating_pipeline.pkl\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee69caa8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "923d8fde",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}