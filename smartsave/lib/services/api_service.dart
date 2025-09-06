import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/transaction.dart';
import '../models/savings_goal.dart';
import '../models/transfer_request.dart';
import '../models/ai_insight.dart';
import '../models/api_response.dart';

class ApiService {
  final String baseUrl =
      'https://smartsave-3iet.onrender.com/'; // Adjust if backend is on different port

  Future<List<Transaction>> getTransactions(String userId,
      {String? startDate, String? endDate}) async {
    final uri = Uri.parse('$baseUrl/transactions/$userId');
    final params = <String, String>{};
    if (startDate != null) params['start_date'] = startDate;
    if (endDate != null) params['end_date'] = endDate;
    final response = await http.get(uri.replace(queryParameters: params));

    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      return data.map((json) => Transaction.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load transactions');
    }
  }

  Future<APIResponse> setSavingsGoal(SavingsGoal goal) async {
    final response = await http.post(
      Uri.parse('$baseUrl/savings-goal'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(goal.toJson()),
    );

    if (response.statusCode == 200) {
      return APIResponse.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to set savings goal');
    }
  }

  Future<APIResponse> transferToSavings(TransferRequest request) async {
    final response = await http.post(
      Uri.parse('$baseUrl/transfer'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(request.toJson()),
    );

    if (response.statusCode == 200) {
      return APIResponse.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to transfer to savings');
    }
  }

  Future<AIInsight> getInsights(String userId) async {
    final response = await http.get(Uri.parse('$baseUrl/insights/$userId'));

    if (response.statusCode == 200) {
      return AIInsight.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to load insights');
    }
  }

  Future<double> getRoundUpSavings(String userId) async {
    final response = await http.get(Uri.parse('$baseUrl/round-up/$userId'));

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      return data['round_up_savings'].toDouble();
    } else {
      throw Exception('Failed to load round-up savings');
    }
  }
}
