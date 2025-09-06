class APIResponse {
  final bool success;
  final String message;
  final Map<String, dynamic>? data;

  APIResponse({
    required this.success,
    required this.message,
    this.data,
  });

  factory APIResponse.fromJson(Map<String, dynamic> json) {
    return APIResponse(
      success: json['success'],
      message: json['message'],
      data: json['data'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'success': success,
      'message': message,
      'data': data,
    };
  }
}
