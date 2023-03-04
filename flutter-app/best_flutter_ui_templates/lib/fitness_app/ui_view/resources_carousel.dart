import 'package:flutter/material.dart';
import '../fitness_app_theme.dart';
import 'package:url_launcher/url_launcher.dart';

class ResourcesCarousel extends StatelessWidget {
  final AnimationController? animationController;
  final Animation<double>? animation;

  ResourcesCarousel({Key? key, this.animationController, this.animation})
      : super(key: key);

  final List<String> images = [
    'https://picsum.photos/seed/picsum/300',
    'https://picsum.photos/seed/picsum/300',
    'https://picsum.photos/seed/picsum/300',
    'https://picsum.photos/seed/picsum/300',
  ];

  final List<String> links = [
    'https://open.spotify.com/track/2gWQbYlLaC04j3teJnFKr9',
    'https://open.spotify.com/track/2gWQbYlLaC04j3teJnFKr9',
    'https://open.spotify.com/track/2gWQbYlLaC04j3teJnFKr9',
    'https://open.spotify.com/track/2gWQbYlLaC04j3teJnFKr9',
  ];

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 200.0,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemCount: images.length,
        itemBuilder: (BuildContext context, int index) {
          return GestureDetector(
            onTap: () {
              // Handle link click
              launchUrl(links[index] as Uri);
            },
            child: Card(
              child: Column(
                children: <Widget>[
                  Image.network(images[index], height: 150.0),
                  Text('Link ${index + 1}'),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
