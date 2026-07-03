from src.features.target import TargetGenerator
from src.data.download import download_nifty_data
from src.data.loader import DataLoader

from src.features.builder import FeatureBuilder
download_nifty_data()

loader = DataLoader()

df = loader.load_market_data()


df = FeatureBuilder.build(df)
df = TargetGenerator.create(df)
print(df.tail())
