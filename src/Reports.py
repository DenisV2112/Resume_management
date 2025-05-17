import json
from datetime import datetime

def reports(curriculum_data, min_experience_years=None, required_qualification=None):
    """
    Exports filtered curriculum reports to JSON files based on given criteria.

    Parameters:
    - curriculum_data (dict): Dictionary with all the CVs.
    - min_experience_years (int): Minimum years of experience to filter (None to skip).
    - required_qualification (str): Required certification or academic qualification (None to skip).
    """

    experience_report = []
    certification_report = []

    for cid, data in curriculum_data.items():
        prof_info = data.get("professional_info", {})
        
        # Filter by experience
        experiences = prof_info.get("profession_experiences", [{}])
        total_months = sum([int(exp["duration_months"]) for exp in experiences[0]]) if experiences else 0
        total_years = total_months / 12

        if min_experience_years is not None and total_years >= min_experience_years:
            experience_report.append({
                "id": cid,
                "name": data["name"],
                "lastname": data["lastname"],
                "experience_years": round(total_years, 2)
            })

        # Filter by certification or training
        certifications = prof_info.get("Certifications", [{}])
        trainings = prof_info.get("academic_training", [{}])
        cert_titles = [cert["qualification"] for cert in certifications[0]] if certifications else []
        training_titles = [train["qualification"] for train in trainings[0]] if trainings else []

        if required_qualification and (required_qualification in cert_titles or required_qualification in training_titles):
            certification_report.append({
                "id": cid,
                "name": data["name"],
                "lastname": data["lastname"],
                "matched_qualification": required_qualification
            })

    # Save experience report
    if min_experience_years is not None:
        with open("report_experience.json", "w", encoding="utf-8") as f:
            json.dump({
                "title": f"Resumes with more than {min_experience_years} years of experience",
                "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "results": experience_report
            }, f, indent=4, ensure_ascii=False)

    # Save certification report
    if required_qualification:
        with open("report_certification.json", "w", encoding="utf-8") as f:
            json.dump({
                "title": f"Resumes with qualification: {required_qualification}",
                "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "results": certification_report
            }, f, indent=4, ensure_ascii=False)

    print("Reports generated successfully.")