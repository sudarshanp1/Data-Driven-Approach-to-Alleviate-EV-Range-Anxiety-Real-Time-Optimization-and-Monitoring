
import statsmodels.api as sm
import pandas as pd

# Sample data
data = pd.DataFrame({
    'driver_id': [1, 2, 3],
    'speed': [50, 60, 70],
    'energy_consumption': [0.5, 0.6, 0.7]
})

# Fixed effects model
model = sm.OLS(data['energy_consumption'], sm.add_constant(data[['speed']]))
results = model.fit()
print(results.summary())
            