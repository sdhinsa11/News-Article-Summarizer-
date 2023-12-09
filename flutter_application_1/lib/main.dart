import 'package:english_words/english_words.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

void main() {
  // every app starts here
  runApp(const MaterialApp(home: FirstRoute()));
}

class FirstRoute extends StatelessWidget {
  // theyy are all widgets
  const FirstRoute({super.key});

  @override
  // tells us what the widget contains
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      // creates state for whole app
      create: (context) => MyAppState(),
      child: MaterialApp(
        title: 'RapidRead',
        theme: ThemeData(
          // material3 - buttons will work a certain way, and be in the color
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.pink),
        ),
        home: MyHomePage(),
        // homepage of app
      ),
    );
  }
}

class MyAppState extends ChangeNotifier {
  var current = WordPair.random();

  void getNext() {
    current = WordPair.random();
    notifyListeners();
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Function to be executed when the "summarize" button is pressed
    void onPressed() {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => const SecondRoute()),
      );
    }

    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "News Summary:", // use here is ur news summary on the next page
              style: TextStyle(
                fontSize: 18.0,
                fontWeight: FontWeight.bold,
              ),
            ),
            MyCustomForm(),
            ElevatedButton(
              onPressed: onPressed,
              child: const Text('Summarize'),
            )
          ],
        ),
      ),
    );
  }
}

// new widget after we refactored (cmd + . (to extract widget))
class MyCustomForm extends StatelessWidget {
  const MyCustomForm({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            SizedBox(height: 16.0),
            TextField(
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Enter news summary',
              ),
              maxLines:
                  10, // Adjust the number of lines according to your needs
              minLines: 1,
            ),
          ],
        ),
      ),
    );
  }
}
//       child: Padding(
//       child: Column(
//         crossAxisAlignment: CrossAxisAlignment.start,
//         children: <Widget>[
//           Padding(
//             padding: EdgeInsets.symmetric(horizontal: 8, vertical: 16),
//             child: SingleChildScrollView(
//               reverse: true,
//               child: Padding(
//                 padding: EdgeInsets.all(32),
//                 child: TextField(
//                   decoration: InputDecoration(
//                     border: OutlineInputBorder(),
//                     hintText: 'Enter news summary',
//                   ),
//                   maxLines: 1000000,
//                   minLines: 1,
//                 ),
//               ),
//             ),
//           ),
//         ],
//       ),
//     ); // SingleChildScrollView will allow me too scroll and see everything while still staying on screen
//   }
// }

class SecondRoute extends StatelessWidget {
  const SecondRoute({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Second Route'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            Navigator.pop(context);
          },
          child: const Text('Go back!'),
        ),
      ),
    );
  }
}
