import os

def extract_names_from_modelnet40():
    """extract names from modelnet40 dataset and save them in .txt file"""
    num_train = 0
    num_test = 0
    with open(os.path.join(dataset_path, 'trainval.txt'), 'w') as trainval_f:
        for shape_name in os.listdir(dataset_path):
            if '.txt' not in shape_name:
                cloud_points_path = os.path.join(dataset_path, shape_name, 'train')
                for cloud_point_name in os.listdir(cloud_points_path):
                    num_train += 1
                    trainval_f.write(os.path.join(shape_name, 'train', cloud_point_name))
                    trainval_f.write('\n')

    with open(os.path.join(dataset_path, 'test.txt'), 'w') as test_f:
        for shape_name in os.listdir(dataset_path):
            if '.txt' not in shape_name:
                cloud_points_path = os.path.join(dataset_path, shape_name, 'test')
                for cloud_point_name in os.listdir(cloud_points_path):
                    num_test +=1
                    test_f.write(os.path.join(shape_name, 'test', cloud_point_name))
                    test_f.write('\n')
    print('The number of train samples is:', num_train)
    print('The number of test samples is:', num_test)


if __name__ == '__main__':
    dataset_path = '../../../data/ModelNet40_ply/'
    extract_names_from_modelnet40()
