import csv
from collections import defaultdict

class ExamResults:
    def __init__(self, input_file):
        self.results = defaultdict(lambda: defaultdict(list))
        with open(input_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                exam_name = row['Exam Name']
                candidate_id = row['Candidate ID']
                score = int(row['Score'])
                self.results[exam_name][candidate_id].append(score)

    def get_summary_stats(self):
        summary_stats = []
        for exam_name in self.results:
            num_candidates = len(self.results[exam_name])
            num_passed = 0
            num_failed = 0
            best_score = 0
            worst_score = float('inf')
            for candidate_scores in self.results[exam_name].values():
                if sum(candidate_scores) >= 150:
                    num_passed += 1
                else:
                    num_failed += 1
                best_score = max(best_score, max(candidate_scores))
                worst_score = min(worst_score, min(candidate_scores))
            summary_stats.append({
                'Exam Name': exam_name,
                'Number of Candidates': num_candidates,
                'Number of Passed Exams': num_passed,
                'Number of Failed Exams': num_failed,
                'Best Score': best_score,
                'Worst Score': worst_score
            })
        return summary_stats

    def write_summary_stats(self, output_file):
        with open(output_file, 'w', newline='') as csv_file:
            field_names = ['Exam Name', 'Number of Candidates', 'Number of Passed Exams', 'Number of Failed Exams', 'Best Score', 'Worst Score']
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
            csv_writer.writeheader()
            for row in self.get_summary_stats():
                csv_writer.writerow(row)
if __name__ == '__main__':
    results = ExamResults('exam_results.csv')
    results.write_summary_stats('exam_summary.csv')