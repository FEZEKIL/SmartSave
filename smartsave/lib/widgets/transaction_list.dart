import 'package:flutter/material.dart';
import '../models/transaction.dart';

class TransactionList extends StatelessWidget {
  final List<Transaction> transactions;

  const TransactionList({super.key, required this.transactions});

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      itemCount: transactions.length,
      itemBuilder: (context, index) {
        final t = transactions[index];
        return ListTile(
          title: Text(t.description),
          subtitle: Text(t.date.toLocal().toString()),
          trailing: Text('\${t.amount.toStringAsFixed(2)}'),
          leading: Icon(
            t.type == 'income' ? Icons.arrow_upward : Icons.arrow_downward,
            color: t.type == 'income' ? Colors.green : Colors.red,
          ),
        );
      },
    );
  }
}
