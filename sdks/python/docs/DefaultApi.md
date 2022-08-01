# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_dashboards_post**](DefaultApi.md#create_dashboard_dashboards_post) | **POST** /dashboards | Create Dashboard
[**create_entry_entries_post**](DefaultApi.md#create_entry_entries_post) | **POST** /entries | Create Entry
[**new_series_series_post**](DefaultApi.md#new_series_series_post) | **POST** /series | New Series

# **create_dashboard_dashboards_post**
> object create_dashboard_dashboards_post(body)

Create Dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.CreateDashboard() # CreateDashboard | 

try:
    # Create Dashboard
    api_response = api_instance.create_dashboard_dashboards_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_dashboard_dashboards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDashboard**](CreateDashboard.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entry_entries_post**
> object create_entry_entries_post(body)

Create Entry

creates a new entry to a series if it exists & the request contains a valid token   :param request: :param data: :return:

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.CreateEntry() # CreateEntry | 

try:
    # Create Entry
    api_response = api_instance.create_entry_entries_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_entry_entries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntry**](CreateEntry.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_series_series_post**
> object new_series_series_post(body)

New Series

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.CreateSeries() # CreateSeries | 

try:
    # New Series
    api_response = api_instance.new_series_series_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->new_series_series_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSeries**](CreateSeries.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

