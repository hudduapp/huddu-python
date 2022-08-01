# SwaggerClient::DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_dashboards_post**](DefaultApi.md#create_dashboard_dashboards_post) | **POST** /dashboards | Create Dashboard
[**create_entry_entries_post**](DefaultApi.md#create_entry_entries_post) | **POST** /entries | Create Entry
[**new_series_series_post**](DefaultApi.md#new_series_series_post) | **POST** /series | New Series

# **create_dashboard_dashboards_post**
> create_dashboard_dashboards_post(body)

Create Dashboard

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::DefaultApi.new
body = SwaggerClient::CreateDashboard.new # CreateDashboard | 


begin
  #Create Dashboard
  api_instance.create_dashboard_dashboards_post(body)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->create_dashboard_dashboards_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDashboard**](CreateDashboard.md)|  | 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json



# **create_entry_entries_post**
> create_entry_entries_post(body)

Create Entry

creates a new entry to a series if it exists & the request contains a valid token   :param request: :param data: :return:

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::DefaultApi.new
body = SwaggerClient::CreateEntry.new # CreateEntry | 


begin
  #Create Entry
  api_instance.create_entry_entries_post(body)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->create_entry_entries_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntry**](CreateEntry.md)|  | 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json



# **new_series_series_post**
> new_series_series_post(body)

New Series

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::DefaultApi.new
body = SwaggerClient::CreateSeries.new # CreateSeries | 


begin
  #New Series
  api_instance.new_series_series_post(body)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->new_series_series_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSeries**](CreateSeries.md)|  | 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json



