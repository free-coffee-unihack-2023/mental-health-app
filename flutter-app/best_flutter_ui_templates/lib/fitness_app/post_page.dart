import 'package:best_flutter_ui_templates/fitness_app/fitness_app_theme.dart';
import 'package:best_flutter_ui_templates/fitness_app/models/journal_entries_data.dart';
import 'package:flutter/material.dart';

class PostPage extends StatefulWidget {
  final String title;
  final String initialContent;
  String noteContent = '';

  PostPage({this.title = '', this.initialContent = ''});

  @override
  _PostPageState createState() => _PostPageState();
}

class _PostPageState extends State<PostPage> {
  final TextEditingController _controller = TextEditingController();

  @override
  void initState() {
    super.initState();
    _controller.text = widget.initialContent;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Journal Entry"),
        backgroundColor: JournalAppTheme.nearlyDarkBlue,
        actions: [
          IconButton(
            onPressed: () {
              // TODO: implement save note
              JournalEntriesData.journalEntriesData.add(
                  JournalEntriesData(
                    time: '03:12 PM',
                    song: 'Arise',
                    songUrl: 'https://open.spotify.com/track/2aaClnypAakdAmLw74JXxB',
                    text: 'fewifskdfn',
                    startColor: '#0a00a2',
                    endColor: '#0a00a2',
                  )
              );
            },
            icon: Icon(Icons.save),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: TextField(
          controller: _controller,
          maxLines: null,
          decoration: InputDecoration(
            border: InputBorder.none,
            hintText: 'Enter text here',
          ),
          style: TextStyle(fontSize: 18.0),
          onChanged: (value) {widget.noteContent = value;},
        ),
      ),
    );
  }
}
