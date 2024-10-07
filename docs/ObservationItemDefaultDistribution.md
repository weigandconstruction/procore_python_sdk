# ObservationItemDefaultDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**login** | **str** | Email | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.observation_item_default_distribution import ObservationItemDefaultDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemDefaultDistribution from a JSON string
observation_item_default_distribution_instance = ObservationItemDefaultDistribution.from_json(json)
# print the JSON string representation of the object
print(ObservationItemDefaultDistribution.to_json())

# convert the object into a dict
observation_item_default_distribution_dict = observation_item_default_distribution_instance.to_dict()
# create an instance of ObservationItemDefaultDistribution from a dict
observation_item_default_distribution_from_dict = ObservationItemDefaultDistribution.from_dict(observation_item_default_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


