# BIMFile1

BIM File Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the issue file | [optional] 
**target_project_id** | **int** | Project that the issue file should be re-associated to. A BIM File can only be re-associated to another project if the file does not have any published models, levels or issues. | [optional] 

## Example

```python
from procore_sdk.models.bim_file1 import BIMFile1

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFile1 from a JSON string
bim_file1_instance = BIMFile1.from_json(json)
# print the JSON string representation of the object
print(BIMFile1.to_json())

# convert the object into a dict
bim_file1_dict = bim_file1_instance.to_dict()
# create an instance of BIMFile1 from a dict
bim_file1_from_dict = BIMFile1.from_dict(bim_file1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


