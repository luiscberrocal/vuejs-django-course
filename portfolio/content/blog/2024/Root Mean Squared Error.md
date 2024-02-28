---
creation date: 2023-10-13 07:23
modification date: 2023-10-13 07:23
tags: 
  - new
toc: true
---

# Root Mean Squared Error

[[Mean Squared Error]] [[Mean Absolute Error]]


```python
import numpy as np

# Actual and Predicted values
actual_values = np.array([22000, 25000, 27000, 21000, 19000])
predicted_values = np.array([23000, 24500, 26900, 21500, 20000])

# Calculating the Mean Absolute Error (MAE)
mae = np.mean(np.abs(actual_values - predicted_values))
mae

# Calculating the Mean Squared Error (MSE)
mse = np.mean((actual_values - predicted_values)**2)
mse

# Calculating the Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
rmse
```

The Root Mean Squared Error (RMSE) for the given example is approximately $708.52

## 1 Interpretation:

- **Magnitude**: The RMSE tells us that, on average, the model's predictions are approximately $708.52 away from the actual values, when considering both small and large errors.
- **Comparative Assessment**: When comparing models, one with a lower RMSE is typically considered better, as it indicates smaller discrepancies between predicted and observed values.
- **Unit Consistency**: Unlike MSE, RMSE is measured in the same unit as the dependent variable ($ in this case), making it more directly interpretable in terms of the magnitude of errors made by the model.
- **Penalty for Larger Errors**: The RMSE penalizes larger errors more severely due to the squaring operation, so an RMSE of $708.52 indicates that the model's larger errors have a substantial impact on this metric.

In summary, while the RMSE provides a sense of the average magnitude of the model’s errors and is quite intuitive due to its unit consistency with the target variable, it should be used alongside other metrics to obtain a holistic view of model performance, especially in the presence of outlier values.
