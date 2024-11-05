import { View, StyleSheet} from 'react-native';
import {Image} from 'expo-image';
import ImageViewer from "@/components/ImageViewer";
import Button from '@/components/Button';
import * as ImagePicker from 'expo-image-picker';
import {useState} from 'react';

const PlaceHolderImage=require("@/assets/images/background-image.png");

export default function Index() {
  const [selectedImage, setSelectedImage]=useState<string|undefined>(undefined);
  const pickImageAsync=async()=>{
    let result=await ImagePicker.launchImageLibraryAsync({
      allowsEditing:true,
      quality:1,
    });
    if (!result.cancelled){
      setSelectedImage(result.assets[0].uri);
    }
    else{
      alert('you did not select any image');
    }
  };
  return (
    <View style={styles.container}>
      <View style={styles.container}>
        <ImageViewer imgSource={PlaceHolderImage} selectedImage={selectedImage}/>
      </View>
      <View style ={styles.footerContainer}>
        <Button theme="primary" label="Choose a photo" onPress={pickImageAsync}/>
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