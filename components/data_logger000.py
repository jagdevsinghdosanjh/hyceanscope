import pandas as pd
from datetime import datetime

# def log_run(mass, radius, temp, composition):
#     log = {
#         "timestamp": datetime.now(),
#         "mass": mass,
#         "radius": radius,
#         "temp": temp,
#         "composition": ",".join(composition)
#     }
#     df = pd.DataFrame([log])
#     df.to_csv("data/logs.csv", mode='a', header=False, index=False)
    
def log_run(student_id, mass, radius, temp, composition):
    from datetime import datetime
    import pandas as pd

    log = {
        "timestamp": datetime.now(),
        "student_id": student_id,
        "mass": mass,
        "radius": radius,
        "temp": temp,
        "composition": ",".join(composition)
    }
    df = pd.DataFrame([log])
    df.to_csv("data/logs.csv", mode='a', header=False, index=False)

def detect_biosignature(composition):
    biosignatures = {"CH3Cl", "DMS"}
    return any(mol in biosignatures for mol in composition)