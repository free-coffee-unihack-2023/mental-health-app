import 'package:flutter/material.dart';
import 'package:flutter_link_previewer/flutter_link_previewer.dart';
import 'package:flutter_chat_types/flutter_chat_types.dart' show PreviewData;
import 'package:url_launcher/url_launcher.dart';

class ResourcesCarousel extends StatefulWidget {
  final AnimationController? animationController;
  final Animation<double>? animation;

  ResourcesCarousel({Key? key, this.animationController, this.animation})
      : super(key: key);

  @override
  _ResourcesCarouselState createState() => _ResourcesCarouselState();
}

class _ResourcesCarouselState extends State<ResourcesCarousel> {

  Map<String, PreviewData> datas = {};
  final String article =
      'https://greatergood.berkeley.edu/article/item/how_journaling_can_help_you_in_hard_times';

  List<String> get urls {
    return const [
      'https://greatergood.berkeley.edu/article/item/how_journaling_can_help_you_in_hard_times',
      'https://www.nytimes.com/2018/10/25/style/journaling-benefits.html',
      'https://www.helpguide.org/articles/mental-health/building-better-mental-health.htm',
      'https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health',
      'https://uhs.umich.edu/tenthings',
      'https://www.healthywa.wa.gov.au/Articles/F_I/Good-mental-health-and-wellbeing',
    ];
  }


  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 400.0,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemBuilder: (BuildContext context, int index) {
          return GestureDetector(
            onTap: () {
              // Handle link click
            },
            child: Card(
              child: Column(
                children: <Widget>[
                  LinkPreview(
                    enableAnimation: true,
                    onPreviewDataFetched: (data) {
                      final String url = urls[index];
                      setState(() {
                        datas = {
                          ...datas,
                          url: data,
                        };
                      });
                    },
                    previewData: datas[urls[index]],
                    text: urls[index],
                    width: MediaQuery.of(context).size.width * 0.8,
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
