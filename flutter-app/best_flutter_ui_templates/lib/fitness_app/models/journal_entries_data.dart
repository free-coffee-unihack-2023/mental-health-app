class JournalEntriesData {
  JournalEntriesData({
    this.time = '',
    this.startColor = '',
    this.endColor = '',
    this.text = '',
    this.song = '',
    this.artist = '',
    this.songUrl = '',
  });

  String time;
  String startColor;
  String endColor;
  String text;
  String song;
  String artist;
  String songUrl;

  static List<JournalEntriesData> journalEntriesData = <JournalEntriesData>[
    JournalEntriesData(
      time: '10:23 AM',
      song: 'Roar',
      artist: 'Katy Perry',
      songUrl: 'https://open.spotify.com/track/27tNWlhdAryQY04Gb2ZhUI',
      text: 'I feel brave and daring today.',
      startColor: '#FA7D82',
      endColor: '#FFB295',
    ),
    JournalEntriesData(
      time: '04:05 PM',
      song: 'Heat Waves',
      artist: 'Glass Animals',
      songUrl: 'https://open.spotify.com/track/6CDzDgIUqeDY5g8ujExx2f',
      text: "It has been a really long day. I probably shouldn't have done it alone",
      startColor: '#738AE6',
      endColor: '#5C5EDD',
    )
  ];
}
