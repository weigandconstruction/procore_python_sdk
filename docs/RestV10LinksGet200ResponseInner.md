# RestV10LinksGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Title | [optional] 
**url** | **str** | URL | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_links_get200_response_inner import RestV10LinksGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10LinksGet200ResponseInner from a JSON string
rest_v10_links_get200_response_inner_instance = RestV10LinksGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10LinksGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_links_get200_response_inner_dict = rest_v10_links_get200_response_inner_instance.to_dict()
# create an instance of RestV10LinksGet200ResponseInner from a dict
rest_v10_links_get200_response_inner_from_dict = RestV10LinksGet200ResponseInner.from_dict(rest_v10_links_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


