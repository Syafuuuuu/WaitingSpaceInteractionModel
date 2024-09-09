
%--- STRANGER SOCIAL INTERACTION MODEL - SSIC MODEL ---%

clc; % clear screen
clear all; % clear all variables & functions
close all; % close figures

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Time settings
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

maxLimY = 1.2;      % graph Y axis max
minLimX = 0;        % graph X axis min
maxLimChangeY = 0.1;
minLimChangeY = -0.1;
numStep =1000;
numStepChange =1000;
dt= 0.1;

k = 0.5; #Psi Cap

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Agent Object
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initialize the 2D array for agents
agentArray = [
    0.1, 0.9, 0.9, 0.1, 0.1, 0.9, 0.9, 0.1, 0.1;
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5;
    0.9, 0.1, 0.1, 0.9, 0.9, 0.1, 0.1, 0.9, 0.9;
    0.9, 0.1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5
];

% Determine the number of agents based on the size of the array
[numAgents, numAttributes] = size(agentArray);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Declare All Variables and Set INITIAL VALUES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Instantaneous
Pa = zeros(numAgents, numStep);
Si = zeros(numAgents, numStep);
Ri = zeros(numAgents, numStep);

%Temporal
Dh = zeros(numAgents, numStep);
Ds = zeros(numAgents, numStep);
Df = zeros(numAgents, numStep);
Li = zeros(numAgents, numStep);
Psi = zeros(numAgents, numStep);

%Difference
dfDh = zeros(numAgents,numStepChange);
dfDs = zeros(numAgents,numStepChange);
dfDf = zeros(numAgents,numStepChange);
dfLi = zeros(numAgents,numStepChange);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Initialisation of all instantaneous parameters

% Positive Affect Para
beta_Pa = 0.2;

% Personality Para
omega_Ps = 0.5;

% Willingness to Interact Para
beta_Si = 0.5;    % Short-Term

% Readiness to Interact Para
omega_Ri = 0.5;
beta_Ri = 1.0;




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Initialisation of all temporal parameters

% Dynamic Emotions Para
gamma_Dh = 0.1;   % Happiness
lambda_Dh = 0.03;
gamma_Ds = 0.1;   % Sadness
lambda_Ds = 0.03;
gamma_Df = 0.1;   % Fear
lambda_Df = 0.03;

% Willingness to Interact Para
gamma_Li = 0.5;   % Long-Term




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Set all Factors
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

           %%% Setting temporal Factors %%%

for i=1:numAgents
  Dh(i, 1) = 0.5;
  Ds(i, 1) = 0.5;
  Df(i, 1) = 0.5;
  Li(i, 1) = 0.5;
endfor



% Now you can use the agents array in your model

for t = 1:numStep
    for i = 1:numAgents
        % Access agent properties using agentArray(i, columnIndex)
        Ha(i, t) = agentArray(i, 1); % Happiness
        Sd(i, t) = agentArray(i, 2); % Sadness
        Fe(i, t) = agentArray(i, 3); % Fear
        Ex(i, t) = agentArray(i, 4); % Extrovertness
        Op(i, t) = agentArray(i, 5); % Openness
        Nu(i, t) = agentArray(i, 6); % Neuroticism
        Eh(i, t) = agentArray(i, 7); % Exhaustion
        Nc(i, t) = agentArray(i, 8); % Cultural Preference
        Ni(i, t) = agentArray(i, 9); % Interest Similarity
    end
end



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Run the model at t=1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for i = 1:numAgents

  % Positive Affect
  Pa(i, 1) = Dh(i, 1) - (beta_Pa * Ds(i, 1));

  % Short Term Willingness to Interact
  Si(i, 1) = beta_Si * Pa(i, 1) + (1 - beta_Si) * (omega_Ps * Ex(i, 1) + (1 - omega_Ps) * Op(i, 1)) * Nc(i, 1) * (1 - Eh(i, 1));

  % Experienced Fear
  Psi(i, 1) = 1 / (1 + exp(-k * (Df(i, 1) * Nu(i, 1))));

  % Interaction Readiness
  Ri(i, 1) = beta_Ri * (omega_Ri * Si(i, 1) + (1 - omega_Ri) * Li(i, 1)) * Ni(i, 1) * (1 - Psi(i, 1));
endfor

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Run the model at t=2
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for t = 2:numStep
  for i=1:numAgents

    % Dynamic Emotions
    Dh(i, t) = Dh(i, t-1) + gamma_Dh * (Ha(i,t-1) - lambda_Dh) * Dh(i, t-1) * (1 - Dh(i, t-1)) * dt;
    Ds(i, t) = Ds(i, t-1) + gamma_Ds * (Sd(i,t-1) - lambda_Ds) * Ds(i, t-1) * (1 - Ds(i, t-1)) * dt;
    Df(i, t) = Df(i, t-1) + gamma_Df * (Fe(i,t-1) - lambda_Df) * Df(i, t-1) * (1 - Df(i, t-1)) * dt;

    % Positive Affect
    Pa(i, t) = Dh(i, t) - (beta_Pa * Ds(i, t));

    % Short Term Willingness to Interact
    Si(i, t) = beta_Si * Pa(i, t) + (1 - beta_Si) * (omega_Ps * Ex(i, t) + (1 - omega_Ps) * Op(i, t)) * Nc(i, t) * (1 - Eh(i, t));

    % Long Term
    Li(i, t) = Li(i,t-1) + gamma_Li * (Si(i,t-1) - Li(i,t-1)) * (1 - Li(i,t-1)) * Li(i,t-1) * dt;

    % Experienced Fear
    Psi(i, t) = 1 / (1 + exp(-k * (Df(i, t) * Nu(i, t))));

    % Interaction Readiness
    Ri(i, t) = beta_Ri * (omega_Ri * Si(i, t) + (1 - omega_Ri) * Li(i, t)) * Ni(i, t) * (1 - Psi(i, t));

  endfor

endfor

% checking equillibria
for t=3:numStepChange
  for i=1:numAgents
    dfDh(i,t) = Dh(i,t-1) - Dh(i, t-2);
    dfDs(i,t) = Ds(i,t-1) - Ds(i, t-2);
    dfDf(i,t) = Df(i,t-1) - Df(i, t-2);
    dfLi(i,t) = Li(i,t-1) - Li(i, t-2);
  endfor
endfor



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                  Graphs
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Temporal Variables
  figure('Name', 'Temporal Factors');
  colormap('jet');

  subplot(2,2,1);
  surf(Dh(1:numAgents,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgents]);zlim([minLimX maxLimY]);
  title('Dynamic Happiness')
  hold on

  subplot(2,2,2);
  surf(Ds(1:numAgents,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgents]);zlim([minLimX maxLimY]);
  title('Dynamic Sadness')
  hold on

  subplot(2,2,3);
  surf(Df(1:numAgents,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgents]);zlim([minLimX maxLimY]);
  title('Dynamic Fear')
  hold on

  subplot(2,2,4);
  surf(Li(1:numAgents,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgents]);zlim([minLimX maxLimY]);
  title('Long-Term Willingness to Interact')
  hold on

% Instantaneous Factors
  figure('Name', 'Instantaneous Factors');
  colormap('jet');

  subplot(2,2,1);
  surf(Pa(1:numAgents,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgents]);zlim([minLimX maxLimY]);
  title('Positive Affect')
  hold on

  subplot(2,2,2);
  surf(Si(1:numAgents,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgents]);zlim([minLimX maxLimY]);
  title('Short-Term Willingness to Interact')
  hold on

  subplot(2,2,3);
  surf(Ri(1:numAgents,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgents]);zlim([minLimX maxLimY]);
  title('Readiness to Interact')
  hold on

  subplot(2,2,4);
  surf(Psi(1:numAgents,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgents]);zlim([minLimX maxLimY]);
  title('Experienced Fear')
  hold on

% graph equillibria
  figure('Name', 'Equillibria State');

  for t=1:numAgents

    subplot(2,4,t);
    plot (dfLi(1, 1:numStepChange),'--*');
    title (['#'  num2str(t)  ' - Long-Term W2I']);
    hold on;

    subplot(2,4,(t+numAgents));
    plot (dfDh(1, 1:numStepChange),'--*');
    title (['#'  num2str(t)  ' - Dynamic Happiness']);

    hold on;
  endfor

##  subplot(2,3,1);
##  plot (dfLi(1, 1:numStepChange),'--*');
##  title ('#1 - Long-Term W2I');
##  hold on;
##
##  subplot(2,3,2);
##  plot (dfLi(2, 1:numStepChange),'--*');
##  title ('#2 - Long-Term W2I');
##  hold on;
##
##  subplot(2,3,3);
##  plot (dfLi(3, 1:numStepChange),'--*');
##  title ('#3 - Long-Term W2I');
##  hold on;
##
##  subplot(2,3,4);
##  plot (dfHa(1, 1:numStepChange),'--*');
##  title ('#1 - Dynamic Happiness');
##  hold on;
##
##  subplot(2,3,5);
##  plot (dfHa(2, 1:numStepChange),'--*');
##  title ('#2 - Dynamic Happiness');
##  hold on;
##
##  subplot(2,3,6);
##  plot (dfHa(3, 1:numStepChange),'--*');
##  title ('#3 - Dynamic Happiness');
##  hold on;

