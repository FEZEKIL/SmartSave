class TransferRequest {
  final String userId;
  final double amount;
  final String toWallet;

  TransferRequest({
    required this.userId,
    required this.amount,
    required this.toWallet,
  });

  Map<String, dynamic> toJson() {
    return {
      'user_id': userId,
      'amount': amount,
      'to_wallet': toWallet,
    };
  }
}
