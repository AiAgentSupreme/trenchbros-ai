import matplotlib.pyplot as plt

def display_risk_score(score):
    colors = ["green", "yellow", "orange", "red"]
    plt.barh(["Risk"], [score], color=colors[min(score // 25, 3)])
    plt.xlim(0, 100)
    plt.title("Risk Score Gauge")
    plt.xlabel("Risk Level")
    plt.show()

# Example usage
if __name__ == "__main__":
    display_risk_score(40)
