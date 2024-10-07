# Links


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | A link back to the current resource | [optional] 
**update** | **str** | A link to the update endpoint for the resource | [optional] 
**delete** | **str** | A link to the delete endpoint for the resource | [optional] 
**permanently_delete** | **str** | A link to the permanent delete endpoint for the resource | [optional] 
**retrieve** | **str** | A link to the retrive endpoint for the resource | [optional] 

## Example

```python
from procore_sdk.models.links import Links

# TODO update the JSON string below
json = "{}"
# create an instance of Links from a JSON string
links_instance = Links.from_json(json)
# print the JSON string representation of the object
print(Links.to_json())

# convert the object into a dict
links_dict = links_instance.to_dict()
# create an instance of Links from a dict
links_from_dict = Links.from_dict(links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


