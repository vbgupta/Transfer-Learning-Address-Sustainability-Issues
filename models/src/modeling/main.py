#-----Main Model File----#
class Model:

    def __init__(self, data):

        self.data = data

    def preprocess(self):

        self.data['License_Class'] = self.data['License_Class'].astype('category').cat.codes
        train = self.data[self.data['year'] != 2021]
        test = self.data[self.data['year'] == 2021]
        print(f"Train Data Years: {train.year.unique()}")
        print(f"Test Data Years: {test.year.unique()}")

        X_train = train.drop(['pm25','aqi'], axis = 1)
        y_train = train[['aqi']]
        X_test = test.drop(['pm25','aqi'], axis = 1)
        y_test = test[['aqi']]

        print(f"X_train Shape: {X_train.shape}")
        print(f"X_test Shape: {X_test.shape}")
        return X_train, y_train, y_test, X_test, train

    def pca(self, train):

        pca = PCA(n_components=5)
        pca.fit(train)
        print(f"explained_variance_ratio_: {pca.explained_variance_ratio_}")
        print(f"singular_values_:{pca.singular_values_}")
        print(f"Components: {pca.components_}")

        return pca

    def build_rfr(self, X_train, y_train, y_test, X_test):

        rfr = RandomForestRegressor(n_estimators=200, criterion="mse", 
                                    min_samples_leaf=3, min_samples_split=3, 
                                    max_depth=10).fit(X_train, y_train)

        print(f"Random Forest Regressor Score: {rfr.score(X_test, y_test) * 100}")

        return rfr

    def build_NN(self, X_train, y_train, X_test, y_test):

        tf.random.set_seed(42)  #first we set random seed
        model = tf.keras.Sequential([
                             tf.keras.layers.Dense(32,activation="relu",input_shape=(32,)),
                             tf.keras.layers.Dense(1)])
        model.compile( loss = tf.keras.losses.mae, #mae stands for mean absolute error
              optimizer = tf.keras.optimizers.SGD(), #stochastic GD
              metrics = ['mae'])
        model.fit(X_train.values.reshape(32, 936), y_train.values.reshape(-1 , 936), epochs = 10)
        predictons = model.evaluate(X_test.values.reshape(32, 318), y_test.values.reshape(-1 ,318))

        return model, predictions

    def plot_preds(self, X_train, y_train, X_test, y_test, model, predictions):
        
        plt.figure(figsize=(12,6))
        plt.scatter(X_train, y_train, c="b", label="Training data")
        plt.scatter(X_test, y_test, c="g", label="Testing data")
        plt.scatter(X_test, predictions, c="r", label="Predictions")
        plt.legend()

        return _

if __name__ == "__main__":

    from database.fetch_data import nyc_v2
    from sklearn.ensemble import RandomForestRegressor
    import pandas as pd
    import warnings
    from sklearn.decomposition import PCA
    import tensorflow as tf

    warnings.filterwarnings("ignore")       
    data = nyc_v2()
    print(data.head())

    model = Model(data)
    X_train, y_train, y_test, X_test, train = model.preprocess()
    pca_analysis  = model.pca(train)
    model_RFR = model.build_rfr( X_train, y_train, y_test, X_test)
    model_NN, predictions = model.build_NN( X_train, y_train, y_test, X_test)
    #plots = model.plot_preds(X_train, y_train, y_test, X_test, model_NN, predictions)