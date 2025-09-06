import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/transaction.dart';
import '../models/ai_insight.dart';
import '../services/api_service.dart';
import '../widgets/transaction_list.dart';
import '../widgets/insight_card.dart';

class DashboardPage extends StatefulWidget {
  const DashboardPage({super.key});

  @override
  State<DashboardPage> createState() => _DashboardPageState();
}

class _DashboardPageState extends State<DashboardPage> {
  late Future<List<Transaction>> _transactionsFuture;
  late Future<AIInsight> _insightFuture;

  final String userId = "user123"; // Placeholder user ID

  @override
  void initState() {
    super.initState();
    final apiService = Provider.of<ApiService>(context, listen: false);
    _transactionsFuture = apiService.getTransactions(userId);
    _insightFuture = apiService.getInsights(userId);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('SmartSave Dashboard'),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Recent Transactions',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            FutureBuilder<List<Transaction>>(
              future: _transactionsFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const CircularProgressIndicator();
                } else if (snapshot.hasError) {
                  return Text('Error: \${snapshot.error}');
                } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
                  return const Text('No transactions found.');
                }
                final transactions = snapshot.data!;
                return TransactionList(transactions: transactions);
              },
            ),
            const SizedBox(height: 24),
            const Text('AI Insights',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            FutureBuilder<AIInsight>(
              future: _insightFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const CircularProgressIndicator();
                } else if (snapshot.hasError) {
                  return Text('Error: \${snapshot.error}');
                } else if (!snapshot.hasData) {
                  return const Text('No insights available.');
                }
                final insight = snapshot.data!;
                return InsightCard(insight: insight);
              },
            ),
          ],
        ),
      ),
    );
  }
}
