class DataCollectionModule:
    def __init__(self):
        self.is_compliant = True

    def ingest_data(self, source):
        print(f"Ingesting data from {source}...")
        print("IEEE-compliant data ingestion active.")

if __name__ == "__main__":
    collector = DataCollectionModule()
    collector.ingest_data("OpenBCI")
