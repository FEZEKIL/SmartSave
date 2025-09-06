import 'package:flutter/material.dart';
import '../models/ai_insight.dart';

class InsightCard extends StatelessWidget {
  final AIInsight insight;

  const InsightCard({super.key, required this.insight});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(insight.message, style: const TextStyle(fontSize: 16)),
            if (insight.recommendation != null) ...[
              const SizedBox(height: 8),
              Text('Recommendation: \${insight.recommendation}',
                  style: const TextStyle(fontWeight: FontWeight.bold)),
            ],
          ],
        ),
      ),
    );
  }
}
