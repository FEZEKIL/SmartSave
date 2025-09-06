class SavingsGoal {
  final String userId;
  final double targetAmount;
  final double currentAmount;
  final DateTime? deadline;

  SavingsGoal({
    required this.userId,
    required this.targetAmount,
    required this.currentAmount,
    this.deadline,
  });

  factory SavingsGoal.fromJson(Map<String, dynamic> json) {
    return SavingsGoal(
      userId: json['user_id'],
      targetAmount: json['target_amount'].toDouble(),
      currentAmount: json['current_amount'].toDouble(),
      deadline:
          json['deadline'] != null ? DateTime.parse(json['deadline']) : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'user_id': userId,
      'target_amount': targetAmount,
      'current_amount': currentAmount,
      'deadline': deadline?.toIso8601String(),
    };
  }
}
