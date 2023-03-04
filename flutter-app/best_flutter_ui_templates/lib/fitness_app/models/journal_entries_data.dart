class JournalEntriesData {
  JournalEntriesData({
    this.time = '',
    this.startColor = '',
    this.endColor = '',
    this.text = '',
    this.song = '',
    this.songUrl = '',
  });

  String time;
  String startColor;
  String endColor;
  String text;
  String song;
  String songUrl;

  static List<JournalEntriesData> journalEntriesData = <JournalEntriesData>[
    JournalEntriesData(
      time: '10:23 AM',
      song: 'Stronger',
      songUrl: '',
      text: 'This is a test of the journal entry. Lorum Ipsum Diam.',
      startColor: '#FA7D82',
      endColor: '#FFB295',
    ),
    JournalEntriesData(
      time: '04:05 PM',
      song: 'Heatwave',
      songUrl: '',
      text: 'Salmon',
      startColor: '#738AE6',
      endColor: '#5C5EDD',
    )
  ];
}
