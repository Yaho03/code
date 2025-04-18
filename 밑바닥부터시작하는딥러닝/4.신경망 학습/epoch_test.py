from keras.datasets import mnist
from keras.utils import to_categorical


(x_train, t_train), (x_test,t_test) = mnist.load_data()
x_train = x_train.reshape(-1, 784)
t_train = to_categorical(t_train)


#하이퍼파라미터
iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

for i in range(iters_num) :
  #미니배치 획득
  batch_mask = np.random.choice(train_size, batch_size)
  x_batch = x_train[batch_mask]
  t_batch = t_train[batch_mask]

  #기울기 계산
  grad = network.numerical_gradient(x_batch, t_batch)

  #매개변수 갱신
  for key in ('W1', 'b1', 'W2', 'b2'):
    network.params[key] -= learning_rate * grad[key]


  #학습 경과 기록
  loss = network.loss(x_batch, t_batch)
  train_loss_list.append(loss)


  if i% iter_per_epoch == 0:
    train_acc = network.accuracy(x_train,t_train)
    test_acc = network.accuracy(x_test,t_test)
    train_acc_list.append(train_acc)
    test_acc_list.append(test_acc)
    print("train acc, test acc |" + str(train_acc) + ", " + str(test_acc))
