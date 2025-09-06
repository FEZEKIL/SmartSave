import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'pages/dashboard_page.dart';
import 'services/api_service.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [Provider<ApiService>(create: (_) => ApiService())],
      child: MaterialApp(
        title: 'SmartSave',
        theme: ThemeData(primarySwatch: Colors.blue),
        home: const DashboardPage(),
        debugShowCheckedModeBanner: false,
      ),
    );
  }
}
