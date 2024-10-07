# Body140


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_file** | [**BIMFile**](BIMFile.md) |  | 

## Example

```python
from procore_sdk.models.body140 import Body140

# TODO update the JSON string below
json = "{}"
# create an instance of Body140 from a JSON string
body140_instance = Body140.from_json(json)
# print the JSON string representation of the object
print(Body140.to_json())

# convert the object into a dict
body140_dict = body140_instance.to_dict()
# create an instance of Body140 from a dict
body140_from_dict = Body140.from_dict(body140_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


