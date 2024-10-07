# RestV10ChangeOrderPackagesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**contract_id** | **int** | Contract ID | 
**change_order** | [**RestV10ChangeOrderPackagesPostRequestChangeOrder**](RestV10ChangeOrderPackagesPostRequestChangeOrder.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_change_order_packages_post_request import RestV10ChangeOrderPackagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderPackagesPostRequest from a JSON string
rest_v10_change_order_packages_post_request_instance = RestV10ChangeOrderPackagesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderPackagesPostRequest.to_json())

# convert the object into a dict
rest_v10_change_order_packages_post_request_dict = rest_v10_change_order_packages_post_request_instance.to_dict()
# create an instance of RestV10ChangeOrderPackagesPostRequest from a dict
rest_v10_change_order_packages_post_request_from_dict = RestV10ChangeOrderPackagesPostRequest.from_dict(rest_v10_change_order_packages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


