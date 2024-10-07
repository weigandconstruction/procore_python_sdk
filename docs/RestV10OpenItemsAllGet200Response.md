# RestV10OpenItemsAllGet200Response

Open items statistics data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**open_count** | **int** |  | [optional] 
**upcoming_count** | **int** |  | [optional] 
**overdue_count** | **int** |  | [optional] 
**last_activity** | **date** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_open_items_all_get200_response import RestV10OpenItemsAllGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10OpenItemsAllGet200Response from a JSON string
rest_v10_open_items_all_get200_response_instance = RestV10OpenItemsAllGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10OpenItemsAllGet200Response.to_json())

# convert the object into a dict
rest_v10_open_items_all_get200_response_dict = rest_v10_open_items_all_get200_response_instance.to_dict()
# create an instance of RestV10OpenItemsAllGet200Response from a dict
rest_v10_open_items_all_get200_response_from_dict = RestV10OpenItemsAllGet200Response.from_dict(rest_v10_open_items_all_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


