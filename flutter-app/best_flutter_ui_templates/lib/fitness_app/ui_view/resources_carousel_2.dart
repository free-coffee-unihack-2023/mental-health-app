import 'package:flutter/material.dart';
import 'package:flutter_link_previewer/flutter_link_previewer.dart';
import 'package:flutter_chat_types/flutter_chat_types.dart' show PreviewData;
import 'package:url_launcher/url_launcher.dart';

class ResourcesCarousel_2 extends StatefulWidget {
  final AnimationController? animationController;
  final Animation<double>? animation;

  ResourcesCarousel_2({Key? key, this.animationController, this.animation})
      : super(key: key);

  @override
  _ResourcesCarousel_2State createState() => _ResourcesCarousel_2State();
}

class _ResourcesCarousel_2State extends State<ResourcesCarousel_2> {

  Map<String, PreviewData> datas = {};
  final String article =
      'https://greatergood.berkeley.edu/article/item/how_journaling_can_help_you_in_hard_times';

  List<String> get urls {
    return const [
      'https://www.headspace.com/sleep/how-to-sleep-better',
      'https://www.webmd.com/sleep-disorders/ss/slideshow-sleep-tips',
      'https://www.cdc.gov/sleep/about_sleep/sleep_hygiene.html',
      'https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/sleep/art-20048379',
      'https://healthysleep.med.harvard.edu/healthy/getting/overcoming/tips',
      'https://www.nhs.uk/every-mind-matters/coronavirus/how-to-fall-asleep-faster-and-sleep-better/',
    ];
  }


  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 500.0,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemBuilder: (BuildContext context, int index) {
          return GestureDetector(
            onTap: () {
              launchUrl(Uri.parse(urls[index]));
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
