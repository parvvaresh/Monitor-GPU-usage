import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, time
import numpy as np

class report_server_weakly:

  def __init__(self,
               df : pd.DataFrame) -> None:


    self.df = df
    self.preprocess()
    print("*** finish pre | process data ***")

  def preprocess(self) -> None:
    """
        steps :

              1 ->  remove null data
              2 -> find name of device
              3 -> convert time columns to datetime type for better work
              4 -> filter office hours and report data for all hours and office hours
              5 -> extract data daily and hourly
                  5.1 -> for all hours
                  5.2 -> for office hours

    """


    self.df = self._remove_null_data(self.df)

    self.name = self._find_name_device(self.df)
    self.df = self._convert_datetime(self.df)

    self.df_filtered = self._filter_office_hours(self.df)


    self.df = self._extract_date_daily(self.df)
    self.df_filtered = self._extract_date_daily(self.df_filtered)


  def get_report_plot(self) -> None:
    self._get_all_7days_in_one_plot(self.df, "utilization.gpu [%]" , list(range(0, 25)), "24")
    self._get_all_7days_in_one_plot(self.df, "utilization.memory [%]" , list(range(0, 25)), "24")


    self.hours_peak_usage(self.df, "utilization.gpu [%]", list(range(1, 25)))
    self.hours_peak_usage(self.df, "utilization.memory [%]", list(range(1, 25)))



    self._get_all_7days_in_one_plot(self.df_filtered, "utilization.gpu [%]" , list(range(7, 16)), "office")
    self._get_all_7days_in_one_plot(self.df_filtered, "utilization.memory [%]" , list(range(7, 16)), "office")


    self.hours_peak_usage(self.df_filtered, "utilization.gpu [%]", list(range(7, 16)))
    self.hours_peak_usage(self.df_filtered, "utilization.memory [%]", list(range(7, 16)))



  def get_text_report(self):


    # for 24 hours

    df = self.df.copy()
    df["hourly"] = self.df["timestamp"].apply(lambda time: time.hour)

    hourly_usage_gou = df.groupby("hourly")["utilization.gpu [%]"].mean()
    peak_hours_gpu = hourly_usage_gou[hourly_usage_gou == hourly_usage_gou.max()].index.tolist()

    hourly_usage_memory = df.groupby("hourly")["utilization.memory [%]"].mean()
    peak_hours_memory = hourly_usage_memory[hourly_usage_memory == hourly_usage_memory.max()].index.tolist()



    #‌ for office hours


    df_filtered = self.df_filtered.copy()

    df_filtered["hourly"] = self.df_filtered["timestamp"].apply(lambda time: time.hour)

    hourly_usage_gou_filtered = df_filtered.groupby("hourly")["utilization.gpu [%]"].mean()
    peak_hours_gpu_filtered = hourly_usage_gou_filtered[hourly_usage_gou_filtered == hourly_usage_gou_filtered.max()].index.tolist()

    hourly_usage_memory_filtered = df_filtered.groupby("hourly")["utilization.memory [%]"].mean()
    peak_hours_memory_filtered = hourly_usage_memory_filtered[hourly_usage_memory_filtered == hourly_usage_memory_filtered.max()].index.tolist()



    text = f"""
                                      - in 24 hours -

                Average use of GPU is :‌ {self.df["utilization.gpu [%]"].mean()}
                Average use of Memory is :‌ {self.df["utilization.memory [%]"].mean()}

                Maximum use of GPU is :‌ {self.df["utilization.gpu [%]"].max()}
                Maximum use of Memory is :‌ {self.df["utilization.memory [%]"].max()}

                Minimum use of GPU is :‌ {self.df["utilization.gpu [%]"].min()}
                Minimum use of Memory is :‌ {self.df["utilization.memory [%]"].min()}
                Peak Hours use GPU is :‌ {peak_hours_gpu}
                Peak Hours use Memory is :‌ {peak_hours_gpu}


                                      - in Office hours -

                Average use of GPU is :‌ {self.df_filtered["utilization.gpu [%]"].mean()}
                Average use of Memory is :‌ {self.df_filtered["utilization.memory [%]"].mean()}

                Maximum use of GPU is :‌ {self.df_filtered["utilization.gpu [%]"].max()}
                Maximum use of Memory is :‌ {self.df_filtered["utilization.memory [%]"].max()}

                Minimum use of GPU is :‌ {self.df_filtered["utilization.gpu [%]"].min()}
                Minimum use of Memory is :‌ {self.df_filtered["utilization.memory [%]"].min()}
                Peak Hours use GPU is :‌ {peak_hours_gpu_filtered}
                Peak Hours use Memory is :‌ {peak_hours_memory_filtered}

    """

    self._print_with_fancy_border(text)


  def _get_all_7days_in_one_plot(self,
                                 df: pd.DataFrame,
                                 column: str,
                                 hourse : list,
                                 title : str):
    df_date = df.groupby(by="date-daily")
    plt.figure(figsize=(20, 12))
    dates = []

    houres_fix = list(map(lambda x: str(x), hourse))

    for date, group in df_date:
      dates.append(date)
      group["hourly"] = group["timestamp"].apply(lambda time: time.hour)

      # Create a series for the 24 hours to ensure all hours are present
      all_hours = pd.Series(index=hourse, dtype=float)
      df_hours = group.groupby(by="hourly")[column].mean()

      # Reindex to ensure all hours are included
      df_hours = df_hours.reindex(all_hours.index, fill_value=np.nan)

      plt.plot(houres_fix, list(df_hours), label=str(date))

    plt.title(f'The amount of {column} usage at different hours (whole day) based on seven days of the week {self.name}')
    plt.xlabel(f'{title} hours a day')
    plt.ylabel('Usage percentage')

    plt.legend()
    plt.show()




  def hours_peak_usage(self,
                       df : pd.DataFrame,
                       column : str,
                       hourse : list) -> None:

    df["hourly"] = df["timestamp"].apply(lambda time: time.hour)

    hourly_usage = df.groupby("hourly")[column].mean()

    peak_hours = hourly_usage[hourly_usage == hourly_usage.max()].index.tolist()
    peak_usage = hourly_usage.max()

    print(f"Peak hours: {peak_hours} with average utilization of {peak_usage}%")

    plt.figure(figsize=(12, 6))
    plt.plot(hourly_usage.index, hourly_usage.values, marker='o', linestyle='-', color='b', label='Average Usage')

    for hour in peak_hours:
        plt.axvline(x=hour, color='r', linestyle='--', label=f'Peak hour: {hour}h')

    plt.title(f'Average {column} Usage by Hour for One Week')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average Utilization (%)')
    plt.xticks(hourse)
    plt.legend()
    plt.grid(True)
    plt.show()


  def _remove_null_data(self, df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

  def _find_name_device(self, df: pd.DataFrame) -> str:
    return df.iloc[0]["name"]  # Assuming 'name' is a column in the dataframe

  def _convert_datetime(self,
                        df: pd.DataFrame) -> pd.DataFrame:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

  def _filter_office_hours(self,
                             df: pd.DataFrame,
                             start_time=time(7, 0, 0),
                             end_time=time(15, 0, 0)) -> pd.DataFrame:
    df_filtered = df[(df['timestamp'].dt.time >= start_time) & (df['timestamp'].dt.time <= end_time)]
    return df_filtered

  def _extract_date_daily(self, df: pd.DataFrame) -> pd.DataFrame:
    df["date-daily"] = df["timestamp"].apply(lambda time: time.date())
    return df

  def _print_with_fancy_border(self,
                              text : str):
      length = len(text)
      top_border = '╔' + '═' * (length + 2) + '╗'
      middle = '║ ' + text + ' ║'
      bottom_border = '╚' + '═' * (length + 2) + '╝'

      print(top_border)
      print(middle)
      print(bottom_border)

