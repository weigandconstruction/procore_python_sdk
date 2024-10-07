# RestV10ChangeOrderRequestsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**contract_id** | **int** | Contract ID | 
**change_order** | [**RestV10ChangeOrderRequestsPostRequestChangeOrder**](RestV10ChangeOrderRequestsPostRequestChangeOrder.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_change_order_requests_post_request import RestV10ChangeOrderRequestsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderRequestsPostRequest from a JSON string
rest_v10_change_order_requests_post_request_instance = RestV10ChangeOrderRequestsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderRequestsPostRequest.to_json())

# convert the object into a dict
rest_v10_change_order_requests_post_request_dict = rest_v10_change_order_requests_post_request_instance.to_dict()
# create an instance of RestV10ChangeOrderRequestsPostRequest from a dict
rest_v10_change_order_requests_post_request_from_dict = RestV10ChangeOrderRequestsPostRequest.from_dict(rest_v10_change_order_requests_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


