# PointNet.pytorch
This repo (https://github.com/fxia22/pointnet.pytorch) is implementation for PointNet(https://arxiv.org/abs/1612.00593) in pytorch. The model is in `pointnet/model.py`. It is tested with pytorch-1.5.0. 

I added codes for extracting names from ModelNet40 and transferring ModelNet40 data from format .off to .ply, which will be convinient for training.

# Download data and running

Download the ModelNet40 dataset in http://modelnet.cs.princeton.edu/ModelNet40.zip

Training 
```
cd utils
python train_classification.py --dataset <dataset path> --nepoch=<number epochs> --dataset_type <modelnet40 | shapenet>
python train_segmentation.py --dataset <dataset path> --nepoch=<number epochs> 
```

Use `--feature_transform` to use feature transform.

# Links
- [Project Page](http://stanford.edu/~rqi/pointnet/)
- [Tensorflow implementation](https://github.com/charlesq34/pointnet)
