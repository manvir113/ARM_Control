import { View, StyleSheet} from 'react-native';
import {Image} from 'expo-image';
import ImageViewer from "@/components/ImageViewer";
import Button from '@/components/Button';

const PlaceHolderImage=require("@/assets/images/background-image.png");

export default function Index() {
  return (
    <View style={styles.container}>
      <View style={styles.container}>
        <ImageViewer imgSource={PlaceHolderImage}/>
      </View>
      <View style ={styles.footerContainer}>
        <Button theme="primary" label="Choose a photo"/>
        <Button label="Use this photo"/>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000000',
    alignItems: 'center',
  },
  text: {
    color: '#fff',
  },
  Image: {
    width: 320,
    height: 440,
    borderRadius: 18,
  },
  footerContainer:{
    flex:1/3,
    alignItems:'center'
  },
});