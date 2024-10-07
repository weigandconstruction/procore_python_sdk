# RestV10LineItemTypesSyncPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[LineItemType1]**](LineItemType1.md) | Array of updated entities | [optional] 
**errors** | **List[object]** | Array of errors | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_line_item_types_sync_patch200_response import RestV10LineItemTypesSyncPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10LineItemTypesSyncPatch200Response from a JSON string
rest_v10_line_item_types_sync_patch200_response_instance = RestV10LineItemTypesSyncPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10LineItemTypesSyncPatch200Response.to_json())

# convert the object into a dict
rest_v10_line_item_types_sync_patch200_response_dict = rest_v10_line_item_types_sync_patch200_response_instance.to_dict()
# create an instance of RestV10LineItemTypesSyncPatch200Response from a dict
rest_v10_line_item_types_sync_patch200_response_from_dict = RestV10LineItemTypesSyncPatch200Response.from_dict(rest_v10_line_item_types_sync_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


