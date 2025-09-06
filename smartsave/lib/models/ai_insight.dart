class AIInsight {
  final String insightType;
  final String message;
  final String? recommendation;

  AIInsight({
    required this.insightType,
    required this.message,
    this.recommendation,
  });

  factory AIInsight.fromJson(Map<String, dynamic> json) {
    return AIInsight(
      insightType: json['insight_type'],
      message: json['message'],
      recommendation: json['recommendation'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'insight_type': insightType,
      'message': message,
      'recommendation': recommendation,
    };
  }
}
